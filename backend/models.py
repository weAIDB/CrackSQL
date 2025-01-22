import datetime
from enum import Enum
from typing import Optional

from config.db_config import db


class DatabaseType(str, Enum):
    """数据库类型枚举"""
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    ORACLE = "oracle"
    
    @classmethod
    def choices(cls):
        """返回选项列表，用于表单选择"""
        return [
            {"value": cls.MYSQL.value, "name": "MySql"},
            {"value": cls.POSTGRESQL.value, "name": "PostgreSQL"},
            {"value": cls.ORACLE.value, "name": "Oracle"}
        ]


class BaseModel:
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now,
        comment="创建时间"
    )
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        onupdate=datetime.datetime.now,
        default=datetime.datetime.now,
        comment="更新时间"
    )


class DatabaseConfig(db.Model, BaseModel):
    """数据库配置表"""
    __tablename__ = 'database_config'
    
    host = db.Column(db.String(128), nullable=False, comment="数据库主机地址")
    port = db.Column(db.Integer, nullable=False, comment="数据库端口")
    database = db.Column(db.String(64), nullable=False, comment="数据库名称")
    username = db.Column(db.String(64), nullable=False, comment="数据库用户名")
    password = db.Column(db.String(256), nullable=False, comment="数据库密码")
    db_type = db.Column(
        db.Enum(DatabaseType),
        nullable=False,
        comment="数据库类型"
    )
    description = db.Column(db.String(256), nullable=True, comment="配置描述")


class User(db.Model, BaseModel):
    """用户表"""
    __tablename__ = 'user'
    
    username = db.Column(db.String(64), unique=True, nullable=False, comment="用户名")
    email = db.Column(db.String(128), unique=True, nullable=True, comment="邮箱")
    nickname = db.Column(db.String(64), nullable=True, comment="用户昵称")
    level = db.Column(
        db.Integer, 
        default=2, 
        comment="用户权限等级(0:超级管理员 1:管理员 2:普通用户)"
    )
    is_active = db.Column(db.Boolean, default=True, comment="是否启用")
    last_login = db.Column(db.DateTime, nullable=True, comment="最后登录时间")


class UserLoginMethod(db.Model, BaseModel):
    """用户登录认证表"""
    __tablename__ = 'user_login_method'
    
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id', ondelete='CASCADE'),
        nullable=False, 
        comment="关联用户ID"
    )
    login_type = db.Column(
        db.String(32), 
        nullable=False, 
        comment="登录类型(username:用户名密码/wechat:微信/mobile:手机号)"
    )
    identifier = db.Column(db.String(128), nullable=False, comment="登录标识(用户名/微信openid/手机号)")
    credential = db.Column(db.String(256), nullable=True, comment="登录凭证(密码hash/token)")
    is_verified = db.Column(db.Boolean, default=False, comment="是否已验证")
    
    # 建立与User模型的关系
    user = db.relationship('User', backref=db.backref('login_methods', lazy=True))


class RewriteStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PROCESSING = "processing"


class RewriteHistory(db.Model, BaseModel):
    """改写历史表"""
    __tablename__ = "rewrite_history"
    
    # 源数据库信息
    source_db_type = db.Column(db.String(50), nullable=False)
    original_sql = db.Column(db.Text, nullable=False)
    
    # 目标数据库信息
    target_db_id = db.Column(
        db.Integer, 
        db.ForeignKey('database_config.id'),
        nullable=False
    )
    target_db_type = db.Column(db.String(50), nullable=False)
    target_db_user = db.Column(db.String(100), nullable=False)
    target_db_host = db.Column(db.String(255), nullable=False)
    target_db_port = db.Column(db.String(10), nullable=False)
    target_db_database = db.Column(db.String(100), nullable=False)
    # 改写结果
    rewritten_sql = db.Column(db.Text)
    status = db.Column(
        db.Enum(RewriteStatus),
        default=RewriteStatus.PROCESSING
    )
    error_message = db.Column(db.Text)


class RewriteProcess(db.Model, BaseModel):
    """改写过程表"""
    __tablename__ = "rewrite_process"
    history_id = db.Column(
        db.Integer, 
        db.ForeignKey('rewrite_history.id'),
        nullable=False
    )
    # 改写过程信息
    step_name = db.Column(db.String(100), nullable=False)
    step_content = db.Column(db.Text)
    intermediate_sql = db.Column(db.Text)
    is_success = db.Column(db.Boolean, default=True)
    error_message = db.Column(db.Text)
    role = db.Column(db.String(20), default='assistant')  # user/system/assistant


class KnowledgeBase(db.Model, BaseModel):
    """知识库模型"""
    __tablename__ = 'knowledge_bases'
    
    kb_name = db.Column(db.String(256), unique=True, nullable=False, comment="知识库名称")
    kb_info = db.Column(db.Text, nullable=True, comment="知识库描述")
    db_type = db.Column(db.String(32), nullable=False, comment="数据库类型:mysql/postgresql/oracle")
    embedding_key = db.Column(db.String(256), nullable=True, default="Description", comment="向量化字段名")
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id', name='fk_knowledge_base_user_id'), 
        nullable=True, 
        comment="创建用户ID"
    )
    collection_id = db.Column(db.String(64), nullable=False, comment="Chroma集合ID")
    embedding_model_name = db.Column(
        db.String(256), 
        db.ForeignKey('llm_models.name', name='fk_knowledge_base_embedding_model'), 
        nullable=False, 
        comment="向量模型名称"
    )

    # 添加关联关系
    embedding_model = db.relationship('LLMModel', backref=db.backref('knowledge_bases', lazy=True), lazy='joined')


class JSONContent(db.Model, BaseModel):
    """JSON内容表"""
    __tablename__ = 'json_contents'
    
    content = db.Column(db.Text, nullable=False, comment="JSON内容")
    content_hash = db.Column(db.String(64), nullable=False, comment="内容哈希值")
    embedding_text = db.Column(db.Text, nullable=True, comment="用于向量化的文本")
    token_count = db.Column(db.Integer, nullable=True, comment="Token数量")
    status = db.Column(db.String(32), default="pending", comment="处理状态:pending/completed/failed")
    error_msg = db.Column(db.Text, nullable=True, comment="错误信息")
    vector_id = db.Column(db.String(64), nullable=True, comment="Chroma向量ID")
    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('user.id', name='fk_json_content_user_id'), 
        nullable=True
    )
    knowledge_base_id = db.Column(
        db.Integer, 
        db.ForeignKey('knowledge_bases.id', name='fk_json_content_knowledge_base_id'), 
        nullable=False, 
        comment="关联知识库ID"
    )


class LLMModel(db.Model, BaseModel):
    """LLM模型配置表"""
    __tablename__ = 'llm_models'
    
    name = db.Column(db.String(256), unique=True, nullable=False, comment="模型名称")
    deployment_type = db.Column(db.String(32), nullable=False, comment="部署类型:local/cloud")
    category = db.Column(db.String(32), nullable=False, comment="模型类型:llm/embedding")
    path = db.Column(db.String(512), nullable=True, comment="本地模型路径")
    api_base = db.Column(db.String(512), nullable=True, comment="API基础URL")
    api_key = db.Column(db.String(256), nullable=True, comment="API密钥")
    temperature = db.Column(db.Float, default=0.7, comment="温度参数")
    max_tokens = db.Column(db.Integer, nullable=True, comment="最大token数")
    dimension = db.Column(db.Integer, nullable=True, comment="向量维度")
    description = db.Column(db.Text, nullable=True, comment="模型描述")
    is_active = db.Column(db.Boolean, default=True, comment="是否启用")
