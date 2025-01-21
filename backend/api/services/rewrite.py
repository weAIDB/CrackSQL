from models import RewriteHistory, RewriteProcess, RewriteStatus
from api.utils.model_to_dict import query_to_dict
from config.db_config import db
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
from config.logging_config import logger


class RewriteService:
    @staticmethod
    def _create_database_url(db_type: str, user: str, password: str, host: str, port: str, database: str) -> str:
        """创建数据库连接URL"""
        password = quote_plus(password)  # 对密码进行URL编码

        if db_type.lower() == 'mysql':
            return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        elif db_type.lower() == 'postgresql':
            return f"postgresql://{user}:{password}@{host}:{port}/{database}"
        elif db_type.lower() == 'oracle':
            # 使用 service_name 方式连接
            return f"oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={database}"
        else:
            raise ValueError(f"不支持的数据库类型: {db_type}")

    @staticmethod
    def test_database_connection(db_type: str, user: str, password: str, host: str, port: str, database: str) -> bool:
        """测试数据库连接"""
        try:
            url = RewriteService._create_database_url(db_type, user, password, host, port, database)
            engine = create_engine(url)

            # 使用 text() 包装 SQL 语句
            with engine.connect() as connection:
                if db_type.lower() == 'oracle':
                    # Oracle 需要使用 text() 包装 SQL
                    result = connection.execute(text("SELECT 1 FROM DUAL"))
                    result.fetchone()  # 确保实际执行了查询
                else:
                    result = connection.execute(text("SELECT 1"))
                    result.fetchone()
            return True

        except SQLAlchemyError as e:
            raise ValueError(f"数据库连接失败: {str(e)}")
        except Exception as e:
            raise ValueError(f"连接过程出现错误: {str(e)}")
        finally:
            if 'engine' in locals():
                engine.dispose()

    @staticmethod
    def create_history(source_db_type: str, original_sql: str,
                      target_db_type: str, target_db_user: str,
                      target_db_host: str, target_db_port: str,
                      target_db_database: str, target_db_password: str,
                      target_db_id: int) -> dict:
        """创建改写历史"""
        
        # 验证目标数据库连接
        try:
            RewriteService.test_database_connection(
                target_db_type,
                target_db_user,
                target_db_password,
                target_db_host,
                target_db_port,
                target_db_database
            )
        except ValueError as e:
            raise ValueError(f"目标数据库连接测试失败: {str(e)}")

        # 创建改写历史记录
        history = RewriteHistory(
            source_db_type=source_db_type,
            original_sql=original_sql,
            target_db_type=target_db_type,
            target_db_user=target_db_user,
            target_db_host=target_db_host,
            target_db_port=target_db_port,
            target_db_database=target_db_database,
            target_db_id=target_db_id,
            status=RewriteStatus.PROCESSING
        )

        db.session.add(history)
        db.session.commit()
        db.session.refresh(history)

        return query_to_dict(history)

    @staticmethod
    def get_history_list(offset, limit, keyword=None):
        query = RewriteHistory.query

        if keyword:
            query = query.filter(RewriteHistory.original_sql.like(f'%{keyword}%'))

        total = query.count()
        histories = query.order_by(RewriteHistory.created_at.desc()) \
            .offset(offset) \
            .limit(limit) \
            .all()
        # 转换为字典并添加processes信息
        result = []
        for history in histories:
            history_dict = query_to_dict(history)
            # 获取关联的processes
            processes = RewriteProcess.query \
                .filter_by(history_id=history.id) \
                .order_by(RewriteProcess.created_at.desc()) \
                .all()
            history_dict['processes'] = [query_to_dict(process) for process in processes]
            result.append(history_dict)

        return {
            'total': total,
            'data': result
        }

    @staticmethod
    def get_history_by_id(history_id):
        history = RewriteHistory.query.filter_by(id=history_id).first()
        if not history:
            return None

        history_dict = query_to_dict(history)
        # 获取关联的processes
        processes = RewriteProcess.query \
            .filter_by(history_id=history.id) \
            .order_by(RewriteProcess.created_at.desc()) \
            .all()
        history_dict['processes'] = [query_to_dict(process) for process in processes]

        return history_dict

    @staticmethod
    def get_latest_history():
        history = RewriteHistory.query.order_by(RewriteHistory.created_at.desc()).first()
        if not history:
            return None

        history_dict = query_to_dict(history)
        # 获取关联的processes
        processes = RewriteProcess.query \
            .filter_by(history_id=history.id) \
            .order_by(RewriteProcess.created_at.desc()) \
            .all()
        history_dict['processes'] = [query_to_dict(process) for process in processes]

        return history_dict

    @staticmethod
    def add_rewrite_process(
        history_id: int,
        content: str,
        step_name: str = None,
        sql: str = None,
        role: str = 'assistant',
        is_success: bool = True,
        error: str = None
    ) -> RewriteProcess:
        """添加改写过程记录
        
        Args:
            history_id: 改写历史ID
            content: 过程内容
            step_name: 步骤名称,如果不提供则自动生成
            sql: SQL语句(如果有)
            role: 角色(assistant/user/system)
            is_success: 是否成功
            error: 错误信息
        """
        try:
            process = RewriteProcess(
                history_id=history_id,
                step_name=step_name,
                step_content=content,
                intermediate_sql=sql,
                role=role,
                is_success=is_success,
                error_message=error
            )
            db.session.add(process)
            db.session.commit()
            return process
            
        except Exception as e:
            logger.error(f"添加改写过程失败: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    def update_rewrite_status(
        history_id: int,
        status: RewriteStatus,
        sql: str = None,
        error: str = None
    ):
        """更新改写状态
        
        Args:
            history_id: 改写历史ID
            status: 新状态
            sql: 改写后的SQL(如果有)
            error: 错误信息(如果有)
        """
        try:
            history = RewriteHistory.query.get(history_id)
            if not history:
                raise ValueError(f"改写历史不存在: {history_id}")
            
            history.status = status
            if sql:
                history.rewritten_sql = sql
            if error:
                history.error_message = error
                
            db.session.commit()
            
        except Exception as e:
            logger.error(f"更新改写状态失败: {str(e)}")
            db.session.rollback()
            raise

    @staticmethod
    async def process_rewrite_task(history_id: int):
        """处理SQL改写任务"""
        try:
            history = RewriteHistory.query.get(history_id)
            if not history:
                raise ValueError(f"改写历史不存在: {history_id}")

            # TODO:调用改写逻辑
            # 异步调用改写的逻辑

            # 以下为改写过程中添加记录和修改改写状态的语句

            # 添加中间记录
            # RewriteService.add_rewrite_process(history_id=history_id, content=history.original_sql, step_name="原始SQL", role='assistant', sql="", is_success=True)

            # 更新改写状态
            #RewriteService.update_rewrite_status(history_id=history_id, status=RewriteStatus.SUCCESS, sql='sql')

        except Exception as e:
            logger.error(f"处理改写任务失败: {str(e)}")
            raise
