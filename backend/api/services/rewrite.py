from models import RewriteHistory, RewriteProcess, RewriteStatus, DatabaseConfig
from config.db_config import db, db_session_manager
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
from config.logging_config import logger
from utils.constants import TOP_K, FAILED_TEMPLATE, MAX_RETRY_TIME, OUT_TYPE, RETRIEVAL_ON


# TODO:
# out_type


class RewriteService:
    @staticmethod
    def _create_database_url(db_type: str, user: str, password: str, host: str, port: str, database: str) -> str:
        """Create database connection URL"""
        password = quote_plus(password)  # URL encode the password

        if db_type.lower() == 'mysql':
            return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        elif db_type.lower() == 'postgresql':
            return f"postgresql://{user}:{password}@{host}:{port}/{database}"
        elif db_type.lower() == 'oracle':
            # Connect using service_name method
            return f"oracle+cx_oracle://{user}:{password}@{host}:{port}/?service_name={database}"
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

    @staticmethod
    def test_database_connection(db_type: str, user: str, password: str, host: str, port: str, database: str) -> bool:
        """Test database connection"""
        try:
            url = RewriteService._create_database_url(db_type, user, password, host, port, database)
            engine = create_engine(url)

            # Use text() to wrap SQL statements
            with engine.connect() as connection:
                if db_type.lower() == 'oracle':
                    # Oracle needs to use text() to wrap SQL
                    result = connection.execute(text("SELECT 1 FROM DUAL"))
                    result.fetchone()  # Ensure the query is actually executed
                else:
                    result = connection.execute(text("SELECT 1"))
                    result.fetchone()
            return True

        except SQLAlchemyError as e:
            raise ValueError(f"Database connection failed: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error occurred during connection: {str(e)}")
        finally:
            if 'engine' in locals():
                engine.dispose()

    @staticmethod
    def create_history(source_db_type: str, original_sql: str, source_kb_id: int, target_kb_id: int, target_db_id: int,
                       llm_model_name: str) -> dict:
        """Create rewrite history"""

        # Validate target database connection
        try:

            target_db = DatabaseConfig.query.get(target_db_id)
            if not target_db:
                raise ValueError(f"Target database does not exist: {target_db_id}")

            # RewriteService.test_database_connection(
            #     target_db.db_type,
            #     target_db.username,
            #     target_db.password,
            #     target_db.host,
            #     target_db.port,
            #     target_db.database
            # )
        except ValueError as e:
            raise ValueError(f"Target database connection test failed: {str(e)}")

        # Create rewrite history record
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
        """Convert RewriteHistory object to dictionary"""
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
        
        # 计算持续时间
        if history.created_at and history.updated_at:
            # 计算时间差（秒）
            time_diff = (history.updated_at - history.created_at).total_seconds()
            
            # 格式化持续时间
            if time_diff < 60:
                duration = f"{int(time_diff)}秒"
            elif time_diff < 3600:
                minutes = int(time_diff // 60)
                seconds = int(time_diff % 60)
                duration = f"{minutes}分{seconds}秒"
            elif time_diff < 86400:
                hours = int(time_diff // 3600)
                minutes = int((time_diff % 3600) // 60)
                duration = f"{hours}小时{minutes}分"
            else:
                days = int(time_diff // 86400)
                hours = int((time_diff % 86400) // 3600)
                duration = f"{days}天{hours}小时"
            
            history_dict['duration'] = duration
        else:
            history_dict['duration'] = "未知"

        # Get associated processes
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
        """Add rewrite process record"""
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
        """Update rewrite status"""
        history = db.session.query(RewriteHistory).get(history_id)
        if not history:
            raise ValueError(f"Rewrite history does not exist: {history_id}")

        history.status = status
        if sql:
            history.rewritten_sql = sql
        if error:
            history.error_message = error
        db.session.commit()

    @staticmethod
    @db_session_manager
    def process_rewrite_task(history_id: int):
        """Process SQL rewrite task"""
        try:
            history = db.session.query(RewriteHistory).get(history_id)
            if not history:
                raise ValueError(f"Rewrite history does not exist: {history_id}")
            try:
                from translate import Translate
                # Original SQL, source database type, source database knowledge base, target database type, target database knowledge base, target database Host, target database Port, target database User, target database Password, LLM-Model-Name
                target_db = DatabaseConfig.query.get(history.target_db_id)
                target_db_config = {
                    "host": target_db.host,
                    "port": target_db.port,
                    "user": target_db.username,
                    "password": target_db.password,
                    "db_name": target_db.database
                }
                vector_config = {
                    "src_kb_name": history.original_kb.kb_name,
                    "tgt_kb_name": history.target_kb.kb_name,
                    "src_embedding_model_name": history.original_kb.embedding_model_name,
                    "tgt_embedding_model_name": history.original_kb.embedding_model_name,
                }

                translate = Translate(model_name=history.llm_model_name, src_sql=history.original_sql,
                                      src_dialect=history.source_db_type.lower(),
                                      tgt_dialect=history.target_db.db_type.lower(),
                                      tgt_db_config=target_db_config, vector_config=vector_config,
                                      history_id=history_id, out_type=OUT_TYPE, retrieval_on=RETRIEVAL_ON, top_k=TOP_K)
                current_sql, model_ans_list, \
                    used_pieces, lift_histories = translate.local_to_global_rewrite(max_retry_time=MAX_RETRY_TIME)

                if current_sql != FAILED_TEMPLATE:
                    RewriteService.add_rewrite_process(
                        history_id=history_id,
                        content=f"The translated SQL is:\n ```{current_sql}```",
                        step_name="Error Message",
                        role='assistant',
                        is_success=False
                    )
                    RewriteService.update_rewrite_status(
                        history_id=history_id,
                        status=RewriteStatus.SUCCESS
                    )
                else:
                    RewriteService.add_rewrite_process(
                        history_id=history_id,
                        content=FAILED_TEMPLATE,
                        step_name="Error Message",
                        role='assistant',
                        is_success=False
                    )
                    RewriteService.update_rewrite_status(
                        history_id=history_id,
                        status=RewriteStatus.FAILED
                    )
            except Exception as e:
                # Update rewrite status to success
                RewriteService.update_rewrite_status(
                    history_id=history_id,
                    status=RewriteStatus.FAILED,
                    error=str(e)
                )
                raise ValueError(f"SQL rewrite failed: {str(e)}")
        except Exception as e:
            logger.error(f"Failed to process rewrite task: {str(e)}")
            # Add error record and update status
            RewriteService.add_rewrite_process(
                history_id=history_id,
                content=str(e),
                step_name="Error Message",
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

    @staticmethod
    @db_session_manager
    def delete_history(history_id: int) -> dict:
        """Delete rewrite history"""
        history = db.session.query(RewriteHistory).get(history_id)
        if not history:
            raise ValueError(f"Rewrite history does not exist: {history_id}")
            
        # Check if the history is in processing status
        if history.status == RewriteStatus.PROCESSING:
            raise ValueError("Cannot delete history in processing status")
            
        # Delete associated processes first
        db.session.query(RewriteProcess).filter_by(history_id=history_id).delete()
        
        # Delete the history record
        db.session.delete(history)
        db.session.commit()
        
        return {"success": True, "message": "History deleted successfully"}
