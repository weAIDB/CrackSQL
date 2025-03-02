import datetime
from enum import Enum

from cracksql.config.db_config import db


class DatabaseType(str, Enum):
    """Database type enumeration"""
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    ORACLE = "oracle"

    @classmethod
    def choices(cls):
        """Return a list of options for form selection"""
        return [
            {"value": cls.MYSQL.value, "name": "MySQL"},
            {"value": cls.POSTGRESQL.value, "name": "PostgreSQL"},
            {"value": cls.ORACLE.value, "name": "Oracle"}
        ]


class BaseModel:
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now, comment="Creation time")
    updated_at = db.Column(db.DateTime, nullable=False, onupdate=datetime.datetime.now, default=datetime.datetime.now,
                           comment="Update time")


class DatabaseConfig(db.Model, BaseModel):
    """Database configuration table"""
    __tablename__ = 'database_config'

    host = db.Column(db.String(128), nullable=False, comment="Database host address")
    port = db.Column(db.Integer, nullable=False, comment="Database port")
    database = db.Column(db.String(64), nullable=False, comment="Database name")
    username = db.Column(db.String(64), nullable=False, comment="Database username")
    password = db.Column(db.String(256), nullable=False, comment="Database password")
    db_type = db.Column(db.Enum(DatabaseType), nullable=False, comment="Database type")
    description = db.Column(db.String(256), nullable=True, comment="Configuration description")


class RewriteStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PROCESSING = "processing"


class RewriteHistory(db.Model, BaseModel):
    """Rewrite history table"""
    __tablename__ = "rewrite_history"

    source_db_type = db.Column(db.String(50), nullable=False, comment="Source database type")
    original_sql = db.Column(db.Text, nullable=False, comment="Original SQL")
    llm_model_name = db.Column(db.String(256),
                               db.ForeignKey('llm_models.name', name='fk_rewrite_history_llm_model_name'),
                               nullable=False, comment="LLM model name")
    original_kb_id = db.Column(db.Integer, db.ForeignKey('knowledge_bases.id',
                                                         name='fk_rewrite_history_original_knowledge_base_id'),
                               nullable=False, comment="Source knowledge base ID")
    target_kb_id = db.Column(db.Integer,
                             db.ForeignKey('knowledge_bases.id', name='fk_rewrite_history_target_knowledge_base_id'),
                             nullable=False, comment="Target knowledge base ID")
    target_db_id = db.Column(db.Integer, db.ForeignKey('database_config.id', name='fk_rewrite_history_target_db_id'),
                             nullable=False, comment="Target database ID")
    rewritten_sql = db.Column(db.Text, comment="Rewritten SQL")
    status = db.Column(db.Enum(RewriteStatus), default=RewriteStatus.PROCESSING, comment="Rewrite status")
    error_message = db.Column(db.Text, comment="Error message")

    # Define relationships explicitly with foreign keys
    original_kb = db.relationship('KnowledgeBase', foreign_keys=[original_kb_id], lazy='joined')
    target_kb = db.relationship('KnowledgeBase', foreign_keys=[target_kb_id], lazy='joined')
    target_db = db.relationship('DatabaseConfig', backref=db.backref("rewrite_histories", lazy=True), lazy='joined')


class RewriteProcess(db.Model, BaseModel):
    """Rewrite process table"""
    __tablename__ = "rewrite_process"
    history_id = db.Column(db.Integer, db.ForeignKey('rewrite_history.id', name='fk_rewrite_process_history_id'),
                           nullable=False, comment="Rewrite history ID")
    step_name = db.Column(db.String(100), nullable=False, comment="Step name")
    step_content = db.Column(db.Text, comment="Step content")
    intermediate_sql = db.Column(db.Text, comment="Intermediate SQL")
    is_success = db.Column(db.Boolean, default=True, comment="Is successful")
    error_message = db.Column(db.Text, comment="Error message")
    role = db.Column(db.String(20), default='assistant', comment="Role: user/system/assistant")


class KnowledgeBase(db.Model, BaseModel):
    """Knowledge base model"""
    __tablename__ = 'knowledge_bases'

    kb_name = db.Column(db.String(256), unique=True, nullable=False, comment="Knowledge base name")
    kb_info = db.Column(db.Text, nullable=True, comment="Knowledge base description")
    db_type = db.Column(db.String(32), nullable=False, comment="Database type: mysql/postgresql/oracle")
    embedding_model_name = db.Column(db.String(256),
                                     db.ForeignKey('llm_models.name', name='fk_knowledge_base_embedding_model'),
                                     nullable=False, comment="Embedding model name")
    # Add relationship
    embedding_model = db.relationship('LLMModel', backref=db.backref('knowledge_bases', lazy=True), lazy='joined')


class JSONContent(db.Model, BaseModel):
    """JSON content table"""
    __tablename__ = 'json_contents'

    content = db.Column(db.Text, nullable=False, comment="JSON content")
    content_type = db.Column(db.String(32), nullable=False, comment="Content type: function/keyword/type/operator")
    content_hash = db.Column(db.String(64), nullable=False, comment="Content hash")
    embedding_text = db.Column(db.Text, nullable=True, comment="Text for vectorization")
    token_count = db.Column(db.Integer, nullable=True, comment="Token count")
    status = db.Column(db.String(32), default="pending", comment="Processing status: pending/completed/failed")
    error_msg = db.Column(db.Text, nullable=True, comment="Error message")
    vector_id = db.Column(db.String(64), nullable=True, comment="Chroma vector ID")
    knowledge_base_id = db.Column(db.Integer,
                                  db.ForeignKey('knowledge_bases.id', name='fk_json_content_knowledge_base_id'),
                                  nullable=False, comment="Associated knowledge base ID")


class LLMModel(db.Model, BaseModel):
    """LLM model configuration table"""
    __tablename__ = 'llm_models'

    name = db.Column(db.String(256), unique=True, nullable=False, comment="Model name")
    deployment_type = db.Column(db.String(32), nullable=False, comment="Deployment type: local/cloud")
    category = db.Column(db.String(32), nullable=False, comment="Model type: llm/embedding")
    path = db.Column(db.String(512), nullable=True, comment="Local model path")
    api_base = db.Column(db.String(512), nullable=True, comment="API base URL")
    api_key = db.Column(db.String(256), nullable=True, comment="API key")
    temperature = db.Column(db.Float, default=0.7, comment="Temperature parameter")
    max_tokens = db.Column(db.Integer, nullable=True, comment="Max tokens")
    dimension = db.Column(db.Integer, nullable=True, comment="Vector dimension")
    description = db.Column(db.Text, nullable=True, comment="Model description")
    is_active = db.Column(db.Boolean, default=True, comment="Is active")
