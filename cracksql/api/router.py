from cracksql.api.database_config import bp as database_config_api
from cracksql.api.rewrite import bp as rewrite_api
from cracksql.api.knowledge import bp as knowledge_api
from cracksql.api.llm_model import bp as llm_model_api

router = [
    database_config_api,  # Database configuration related interfaces
    rewrite_api,  # Rewrite related interfaces
    knowledge_api,  # Knowledge base related interfaces
    llm_model_api  # Model management interfaces
]
