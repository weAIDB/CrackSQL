from api.user import bp as user_api
from api.database_config import bp as database_config_api
from api.file import bp as file_api
from api.rewrite import bp as rewrite_api
from api.knowledge import bp as knowledge_api
from api.llm_model import bp as llm_model_api

router = [
    user_api,  # 用户相关接口
    database_config_api,  # 数据库配置相关接口
    file_api,  # 文件操作相关接口
    rewrite_api,  # 重写相关接口
    knowledge_api,  # 知识库相关接口
    llm_model_api  # 模型管理接口
]
