from models import RewriteHistory, RewriteProcess, RewriteStatus, DatabaseConfig
from config.db_config import db, db_session_manager
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
from config.logging_config import logger
from utils.constants import TOP_K, FAILED_TEMPLATE


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
    def create_history(source_db_type: str, original_sql: str, source_kb_id: int, target_kb_id: int, target_db_id: int,
                       llm_model_name: str) -> dict:
        """创建改写历史"""

        # 验证目标数据库连接
        try:

            target_db = DatabaseConfig.query.get(target_db_id)
            if not target_db:
                raise ValueError(f"目标数据库不存在: {target_db_id}")

            # RewriteService.test_database_connection(
            #     target_db.db_type,
            #     target_db.username,
            #     target_db.password,
            #     target_db.host,
            #     target_db.port,
            #     target_db.database
            # )
        except ValueError as e:
            raise ValueError(f"目标数据库连接测试失败: {str(e)}")

        # 创建改写历史记录
        history = RewriteHistory(
            source_db_type=source_db_type,
            original_sql=original_sql,
            original_kb_id=source_kb_id,
            target_kb_id=target_kb_id,
            target_db_id=target_db_id,
            llm_model_name=llm_model_name,
            status=RewriteStatus.PROCESSING
        )

        db.session.add(history)
        db.session.commit()
        db.session.refresh(history)

        return {"id": history.id}

    @staticmethod
    def _convert_history_to_dict(history):
        """将 RewriteHistory 对象转换为字典"""
        if not history:
            return None

        history_dict = {
            'id': history.id,
            'source_db_type': history.source_db_type,
            'original_sql': history.original_sql,
            'original_kb': {
                'id': history.original_kb.id,
                'name': history.original_kb.kb_name,
            },
            'target_kb': {
                'id': history.target_kb.id,
                'name': history.target_kb.kb_name
            },
            'target_db': {
                'id': history.target_db.id,
                'database': history.target_db.database,
                'host': history.target_db.host,
                'port': history.target_db.port,
                'username': history.target_db.username,
                'db_type': history.target_db.db_type
            },
            'llm_model_name': history.llm_model_name,
            'status': history.status,
            'created_at': history.created_at,
            'updated_at': history.updated_at,
            'error_message': history.error_message,
            'rewritten_sql': history.rewritten_sql
        }

        # 获取关联的processes
        processes = RewriteProcess.query \
            .filter_by(history_id=history.id) \
            .all()

        history_dict['processes'] = [{
            'id': process.id,
            'history_id': process.history_id,
            'step_name': process.step_name,
            'step_content': process.step_content,
            'intermediate_sql': process.intermediate_sql,
            'is_success': process.is_success,
            'error_message': process.error_message,
            'role': process.role,
            'created_at': process.created_at,
            'updated_at': process.updated_at
        } for process in processes]

        return history_dict

    @staticmethod
    def get_history_list(offset, limit, keyword=None):

        if keyword:
            query = RewriteHistory.query.filter(RewriteHistory.original_sql.like(f'%{keyword}%'))
        else:
            query = RewriteHistory.query

        total = query.count()
        histories = query.order_by(RewriteHistory.created_at.desc()) \
            .offset(offset) \
            .limit(limit) \
            .all()

        print(histories)

        result = [RewriteService._convert_history_to_dict(history) for history in histories]

        return {
            'total': total,
            'data': result
        }

    @staticmethod
    def get_history_by_id(history_id):
        history = RewriteHistory.query.filter_by(id=history_id).first()
        return RewriteService._convert_history_to_dict(history)

    @staticmethod
    def get_latest_history():
        history = RewriteHistory.query.order_by(RewriteHistory.created_at.desc()).first()
        return RewriteService._convert_history_to_dict(history)

    @staticmethod
    @db_session_manager
    def add_rewrite_process(
            history_id: int,
            content: str,
            step_name: str = None,
            sql: str = None,
            role: str = 'assistant',
            is_success: bool = True,
            error: str = None
    ) -> RewriteProcess:
        """添加改写过程记录"""
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

    @staticmethod
    @db_session_manager
    def update_rewrite_status(
            history_id: int,
            status: RewriteStatus,
            sql: str = None,
            error: str = None
    ):
        """更新改写状态"""
        history = db.session.query(RewriteHistory).get(history_id)
        if not history:
            raise ValueError(f"改写历史不存在: {history_id}")

        history.status = status
        if sql:
            history.rewritten_sql = sql
        if error:
            history.error_message = error
        db.session.commit()

    @staticmethod
    @db_session_manager
    def process_rewrite_task(history_id: int):
        """处理SQL改写任务"""
        try:
            history = db.session.query(RewriteHistory).get(history_id)
            if not history:
                raise ValueError(f"改写历史不存在: {history_id}")
            try:
                from translate import Translate
                # 原始SQL，源数据库类型，源数据库知识库，目标数据库类型，目标数据库知识库，目标数据库Host，目标数据库Port，目标数据库User，目标数据库Password, LLm-Model-Name
                target_db = DatabaseConfig.query.get(history.target_db_id)
                target_db_config = {
                    "host": target_db.host,
                    "port": target_db.port,
                    "user": target_db.username,
                    "password": target_db.password,
                    "db_name": target_db.database
                }
                embedding_config = {
                    "src_embedding_model_name": history.source_db_type.lower(),
                    "tgt_embedding_model_name": history.target_db.db_type.lower()
                }
                vector_config = {
                    "src_collection_id": history.original_kb.collection_id,
                    "tgt_collection_id": history.target_kb.collection_id,
                    "top_k": TOP_K
                }

                translate = Translate(model_name=history.llm_model_name, src_sql=history.original_sql,
                                      src_dialect=history.source_db_type.lower(),
                                      tgt_dialect=history.target_db.db_type.lower(), tgt_db_config=target_db_config,
                                      embedding_config=embedding_config, vector_config=vector_config,
                                      history_id=history_id, out_type="db", retrieval_on=True)
                now_sql, model_ans_list, used_pieces, lift_histories = translate.local_rewrite(max_retry_time=2)
                print(now_sql)
                RewriteService.add_rewrite_process(
                    history_id=history_id,
                    content=f"```{str(now_sql)}```",
                    step_name="错误信息",
                    role='assistant',
                    is_success=False
                )

                if now_sql != FAILED_TEMPLATE:
                    RewriteService.update_rewrite_status(
                        history_id=history_id,
                        status=RewriteStatus.SUCCESS
                    )
                else:
                    RewriteService.update_rewrite_status(
                        history_id=history_id,
                        status=RewriteStatus.FAILED
                    )
            except Exception as e:
                # 更新改写状态为成功
                RewriteService.update_rewrite_status(
                    history_id=history_id,
                    status=RewriteStatus.FAILED,
                    error=str(e)
                )
                raise ValueError(f"SQL改写失败: {str(e)}")
        except Exception as e:
            logger.error(f"处理改写任务失败: {str(e)}")
            # 添加错误记录和更新状态
            RewriteService.add_rewrite_process(
                history_id=history_id,
                content=str(e),
                step_name="错误信息",
                role='system',
                is_success=False,
                error=str(e)
            )
            RewriteService.update_rewrite_status(
                history_id=history_id,
                status=RewriteStatus.FAILED,
                error=str(e)
            )
            raise
