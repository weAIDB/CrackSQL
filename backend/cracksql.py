from init_knowledge_base import initialize_kb
from translate import Translator
from app_factory import create_app
from typing import Dict, List, Tuple, Union, Optional
from api.services.llm_model import LLMModelService


def add_llm_model(name: str, deployment_type: str, path: str, api_base: str, api_key: str, temperature: float, max_tokens: int, description: str, is_active: bool = True):
    """
    Add a new LLM model to the database
    
    Args:
        name (str): Name of the LLM model 
        deployment_type (str): Deployment type: local/cloud
        path (str): Local model path
        api_base (str): API base URL
        api_key (str): API key
        temperature (float): Temperature parameter
        max_tokens (int): Maximum tokens of the LLM model
        description (str): Model description
        is_active (bool): Whether the LLM model is active
    
    Returns:
        bool: Whether the LLM model is added successfully
    """
    try:
        if not name:
            raise ValueError("name is required")
        if not deployment_type:
            raise ValueError("deployment_type is required")
        
        if deployment_type == "local" and not path:
            raise ValueError("path is required")
        
        if deployment_type == "cloud" and not api_base:
            raise ValueError("api_base is required")
        
        data = {
            "name": name,
            "path": path,
            "api_base": api_base,
            "api_key": api_key,
            "deployment_type": deployment_type,
            "category": "llm",
            "description": description,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "dimension": 0,
            "is_active": is_active
        }
        res = LLMModelService.create_model(data)
        if res:
            return True
        else:
            print(f"Failed to add LLM model: {res}")
            return False
    except Exception as e:
        print(f"Failed to add LLM model: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def add_embedding_model(name: str, deployment_type: str, path: str, api_base: str, api_key: str, dimension: int, description: str, is_active: bool = True):
    """
    Add a new embedding model to the database
    
    Args:
        name (str): Name of the embedding model
        deployment_type (str): Deployment type: local/cloud
        path (str): Local model path
        api_base (str): API base URL
        api_key (str): API key
        dimension (int): Dimension of the embedding model
        description (str): Model description
        is_active (bool): Whether the embedding model is active
    Returns:
        bool: Whether the embedding model is added successfully
    """

    try:
        if not name:
            raise ValueError("name is required")
        if not deployment_type:
            raise ValueError("deployment_type is required")
        
        if deployment_type == "local" and not path:
            raise ValueError("path is required")
        
        if deployment_type == "cloud" and not api_base:
            raise ValueError("api_base is required")
        
        data = {
            "name": name,
            "path": path,
            "api_base": api_base,
            "api_key": api_key,
            "deployment_type": deployment_type,
            "category": "embedding",
            "description": description,
            "dimension": dimension,
            "is_active": is_active
        }
        res = LLMModelService.create_model(data)
        if res:
            return True
        else:
            print(f"Failed to add embedding model: {res}")
            return False
    except Exception as e:
        print(f"Failed to add embedding model: {str(e)}")
        import traceback
        traceback.print_exc()
        return False



def translate(
    src_sql: str, 
    src_dialect: str, 
    tgt_dialect: str, 
    model_name: str = "llama3.3", 
    target_db_config: Optional[Dict] = None, 
    vector_config: Optional[Dict] = None,
    out_dir: str = "./", 
    retrieval_on: bool = False, 
    top_k: int = 3,
    max_retry_time: int = 3
) -> Union[str, Tuple[str, List, List, List]]:
    """
    Translate source SQL from one database dialect to target database dialect
    
    Args:
        src_sql (str): Source SQL statement to be translated, required
        src_dialect (str): Source database dialect (mysql, postgresql, oracle, etc.), required
        tgt_dialect (str): Target database dialect (mysql, postgresql, oracle, etc.), required
        model_name (str): Language model name to use, required, needs to be configured in initkb
        target_db_config (Dict, optional): Target database configuration, required, format: {"host": "127.0.0.1", "port": 3306, "user": "root", "password": "123456", "db_name": "test"}
        vector_config (Dict, optional): Vector storage configuration, required, format: {"src_kb_name": "postgresql_knowledge", "tgt_kb_name": "mysql_knowledge"}
        out_dir (str): Output directory path, default is "./"
        retrieval_on (bool): Whether to enable knowledge retrieval, default is False
        top_k (int): Number of top k relevant documents to return during retrieval, default is 3
        max_retry_time (int): Maximum retry times, default is 3
    
    Returns:
        Union[str, Tuple[str, List, List, List]]: Translated SQL, model answer list, used knowledge pieces, lift history
    """

    if not model_name:
        raise ValueError("model_name is required")
    
    if not src_sql:
        raise ValueError("src_sql is required")
    
    if not src_dialect:
        raise ValueError("src_dialect is required")
    
    if not tgt_dialect:
        raise ValueError("tgt_dialect is required")
    
    if not target_db_config or not target_db_config.get("host", None):
        raise ValueError("target_db_config is required")
    
    if not vector_config or not vector_config.get("src_kb_name", None) or not vector_config.get("tgt_kb_name", None):
        raise ValueError("vector_config is required")
    
    app = create_app("PRODUCTION")
    app.config["SCHEDULER_OPEN"] = False
    
    with app.app_context():
        translator = Translator(
            model_name=model_name, 
            src_sql=src_sql,
            src_dialect=src_dialect,
            tgt_dialect=tgt_dialect, 
            tgt_db_config=target_db_config, 
            vector_config=vector_config,
            history_id="", 
            out_type="file", 
            out_dir=out_dir, 
            retrieval_on=retrieval_on, 
            top_k=top_k
        )
        
        return translator.local_to_global_rewrite(max_retry_time=max_retry_time)

def initkb(config_file_path: Optional[str] = None) -> bool:
    """
    Initialize knowledge base
    
    Args:
        config_file_path (str, optional): Knowledge base config file path, required
    
    Returns:
        bool: Whether initialization succeeded
    """
    try:
        if config_file_path is None:
            raise ValueError("config_file_path is required")
        
        initialize_kb(config_file_path)
        return True
    except Exception as e:
        print(f"Knowledge base initialization failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
