from typing import List, Optional, Dict, Any
from models import LLMModel
from config.db_config import db
from sqlalchemy import or_
from llm_model.llm_manager import llm_manager
from llm_model.embeddings import embedding_manager

class LLMModelService:
    """LLM model service"""

    @staticmethod
    def create_model(data: Dict[str, Any]) -> LLMModel:
        """Create model"""
        required_fields = ['name', 'deployment_type']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        try:
            deployment_type = data['deployment_type']
        except ValueError:
            raise ValueError(f"无效的模型类型: {data['deployment_type']}")

        if deployment_type == "local" and not data.get('path'):
            raise ValueError("Local model must provide model path")
        if deployment_type == "cloud" and not data.get('api_base'):
            raise ValueError("Cloud model must provide API base URL")

        model = LLMModel(
            name=data['name'],
            deployment_type=deployment_type,
            category=data['category'],
            path=data.get('path'),
            api_base=data.get('api_base'),
            api_key=data.get('api_key'),
            temperature=data.get('temperature', 0.7),
            max_tokens=data.get('max_tokens'),
            description=data.get('description'),
            dimension=data.get('dimension'),
            is_active=data.get('is_active', True)
        )

        db.session.add(model)
        db.session.commit()
        return {
            'id': model.id,
            'name': model.name,
            'deployment_type': model.deployment_type,
            'category': model.category,
            'path': model.path,
            'api_base': model.api_base,
            'temperature': model.temperature,
            'max_tokens': model.max_tokens,
            'dimension': model.dimension,
            'description': model.description,
            'is_active': model.is_active
        }

    @staticmethod
    def update_model(model_id: int, data: Dict[str, Any]) -> Optional[LLMModel]:
        """Update model"""
        model = LLMModel.query.get(model_id)
        if not model:
            return None

        for key, value in data.items():
            if hasattr(model, key) and key != 'id':
                setattr(model, key, value)

        db.session.commit()
        # Reload model
        llm_manager.reload_model(model.name)
        return {
            'id': model.id,
            'name': model.name,
            'deployment_type': model.deployment_type,
            'category': model.category,
            'path': model.path,
            'api_base': model.api_base,
            'temperature': model.temperature,
            'max_tokens': model.max_tokens,
            'description': model.description,
            'dimension': model.dimension,
            'is_active': model.is_active
        }

    @staticmethod
    def delete_model(model_id: int) -> bool:
        """Delete model"""
        model = LLMModel.query.get(model_id)
        if not model:
            return False

        db.session.delete(model)
        db.session.commit()
        return True

    @staticmethod
    def get_models(
            page: int = 1,
            per_page: int = 10,
            search: Optional[str] = None,
            deployment_type: Optional[str] = None,
            category: Optional[str] = None,
            is_active: Optional[bool] = None
    ) -> tuple[List[LLMModel], int]:
        """Get model list"""
        query = LLMModel.query

        if search:
            query = query.filter(
                or_(
                    LLMModel.name.ilike(f"%{search}%"),
                    LLMModel.description.ilike(f"%{search}%")
                )
            )

        if deployment_type:
            try:
                query = query.filter(LLMModel.deployment_type == deployment_type)
            except ValueError:
                raise ValueError(f"无效的模型类型: {deployment_type}")

        if category:
            query = query.filter(LLMModel.category == category)

        if is_active is not None:
            query = query.filter(LLMModel.is_active == is_active)

        total = query.count()

        query = query.order_by(LLMModel.created_at.desc())
        query = query.offset((page - 1) * per_page).limit(per_page)
        models = query.all()

        return [{
            'id': model.id,
            'name': model.name,
            'deployment_type': model.deployment_type,
            'category': model.category,
            'path': model.path,
            'api_base': model.api_base,
            'api_key': model.api_key,
            'temperature': model.temperature,
            'max_tokens': model.max_tokens,
            'description': model.description,
            'dimension': model.dimension,
            'is_active': model.is_active
        } for model in models], total


    @staticmethod
    def release_all_llm_models():
        """Release all models"""
        llm_manager.release_all_models()

    @staticmethod
    def release_llm_model(model_name: str):
        """Release model"""
        llm_manager.release_model(model_name)

    @staticmethod
    def load_llm_model(model_name: str):
        """Load model"""
        llm_manager.get_model(model_name)

    @staticmethod
    def load_embedding(model_name: str):
        """Load Embedding model"""
        embedding_manager.get_embedding(model_name)

    @staticmethod
    def release_all_embeddings():
        """Release all Embedding models"""
        embedding_manager.release_all_embeddings()

    @staticmethod
    def release_embedding(model_name: str):
        """Release Embedding model"""
        embedding_manager.release_embedding(model_name)
        
