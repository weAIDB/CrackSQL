from typing import Dict, Optional
from .base import BaseLLM
from .implementations import CloudLLM, LocalLLM
from models import LLMModel
import logging
from config.db_config import db_session_manager


logger = logging.getLogger(__name__)


class LLMManager:
    """LLM model manager"""

    def __init__(self):
        self._models: Dict[str, BaseLLM] = {}

    def load_model(self, model_config: Dict) -> Optional[BaseLLM]:
        """
        Load a single model
        Args:
            config: Model configuration
        Returns:
            Optional[BaseLLM]: The loaded model instance
        """
        try:
            # Create a model instance based on the type
            model_cls = CloudLLM if model_config['deployment_type'] == 'cloud' else LocalLLM
            model = model_cls(model_config)

            # Validate configuration
            if not model.validate_config():
                logger.error(f"Invalid model configuration: {model_config['name']}")
                return None

            self._models[model_config['name']] = model
            logger.info(f"Successfully loaded model: {model_config['name']}")
            return model

        except Exception as e:
            logger.error(f"Failed to load model {model_config['name']}: {str(e)}")
            return None
    

    @db_session_manager
    def get_model_config_from_db(self, name: str) -> Optional[Dict]:
        """Get model configuration from database"""
        config = LLMModel.query.filter_by(name=name).first()
        if not config:
            logger.error(f"Model configuration does not exist: {name}")
            return None
        if not config.is_active:
            logger.error(f"Model is not enabled: {name}")
            return None

        model_config = {
            'name': config.name,
            'deployment_type': config.deployment_type,
            'category': config.category,
            'temperature': config.temperature,
            'max_tokens': config.max_tokens,
            'model_path': config.path,
            'api_base': config.api_base,
            'api_key': config.api_key
        }

        return model_config


    def reload_model(self, name: str, config: Optional[Dict] = None) -> Optional[BaseLLM]:
        """
        Reload model
        Args:
            name: Model name
            config: Optional model configuration dictionary
        Returns:
            Optional[BaseLLM]: The reloaded model instance
        """
        if name not in self._models:
            logger.error(f"Model does not exist: {name}, no need to reload")

        # Release model, after release, the model will be destroyed
        # self._models[name].release()

        # Reload model
        return self.get_model(name, config)


    def get_model(self, name: str, config: Optional[Dict] = None) -> Optional[BaseLLM]:
        """Get model instance
        Args:
            name: Model name
            config: Optional model configuration dictionary
        Returns:
            Optional[BaseLLM]: The model instance
        """
        if name not in self._models:
            if config is None:
                config = self.get_model_config_from_db(name)
                if not config:
                    logger.error(f"Model configuration does not exist: {name}")
                    return None
            else:
                # Use dictionary access method
                if config['deployment_type'] == 'cloud' and (config.get('api_base') is None or config.get('api_key') is None):
                    logger.error(f"Model configuration parameters are incomplete: {config['name']}")
                    return None
                elif config['deployment_type'] == 'local' and config.get('model_path') is None:
                    logger.error(f"Model configuration parameters are incomplete: {config['name']}")
                    return None
            return self.load_model(config)
        return self._models.get(name)


    def release_model(self, model_name: str):
        """Release model"""
        if model_name in self._models:
            self._models[model_name].release()
            del self._models[model_name]

    def release_all_models(self):
        """Release all models"""
        for model_name in self._models:
            self._models[model_name].release()
        self._models.clear()

# Global LLM manager instance
llm_manager = LLMManager()
