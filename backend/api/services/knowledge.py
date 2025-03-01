from models import KnowledgeBase, JSONContent, LLMModel
from config.db_config import db
from config.logging_config import logger
from typing import List, Dict
import os
import asyncio
import json
from flask import current_app
import time
from llm_model.embeddings import get_embeddings
from vector_store.chroma_store import ChromaStore
import hashlib
import tiktoken


def get_knowledge_base_list() -> List[Dict]:
    """Get knowledge base list"""
    try:
        knowledge_bases = KnowledgeBase.query.all()
        if not knowledge_bases:
            return []

        result = []
        for kb in knowledge_bases:
            kb_dict = {
                "id": kb.id,
                "kb_name": kb.kb_name,
                "kb_info": kb.kb_info,
                "embedding_model_name": kb.embedding_model_name,
                "created_at": kb.created_at.strftime("%Y-%m-%d %H:%M:%S") if kb.created_at else None,
                "updated_at": kb.updated_at.strftime("%Y-%m-%d %H:%M:%S") if kb.updated_at else None,
                "db_type": kb.db_type,
            }
            result.append(kb_dict)
        return result
    except Exception as e:
        logger.error(f"get_knowledge_base_list error: {e}")
        raise


def get_knowledge_base(kb_name: str) -> Dict:
    """Get a single knowledge base"""
    try:
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            return None

        return {
            "id": kb.id,
            "kb_name": kb.kb_name,
            "kb_info": kb.kb_info,
            "embedding_model": {
                "id": kb.embedding_model.id,
                "name": kb.embedding_model.name,
                "dimension": kb.embedding_model.dimension,
                "category": kb.embedding_model.category,
                "deployment_type": kb.embedding_model.deployment_type,
                "description": kb.embedding_model.description
            } if kb.embedding_model else None,
            "db_type": kb.db_type,
            "created_at": kb.created_at.strftime("%Y-%m-%d %H:%M:%S") if kb.created_at else None,
            "updated_at": kb.updated_at.strftime("%Y-%m-%d %H:%M:%S") if kb.updated_at else None
        }
    except Exception as e:
        logger.error(f"get_knowledge_base error: {e}")
        raise


def create_knowledge_base(kb_name: str, kb_info: str, embedding_model_name: str, db_type: str) -> Dict:
    """Create a knowledge base"""
    try:
        # Check if the knowledge base name already exists
        if KnowledgeBase.query.filter_by(kb_name=kb_name).first():
            return {
                "status": False,
                "msg": f"Knowledge base '{kb_name}' already exists"
            }   

        # Get LLMModel instance
        embedding_model = LLMModel.query.filter_by(
            name=embedding_model_name,
            category='embedding',
            is_active=True
        ).first()

        if not embedding_model:
            return {
                "status": False,
                "msg": "Invalid embedding model"
            }

        # Create knowledge base
        kb = KnowledgeBase(
            kb_name=kb_name,
            kb_info=kb_info,
            embedding_model_name=embedding_model_name,
            db_type=db_type
        )
        db.session.add(kb)
        db.session.commit()

        return {
            "status": True,
            "data": {
                "kb_name": kb.kb_name,
                "kb_info": kb.kb_info,
                "embedding_model_name": kb.embedding_model_name,
                "db_type": kb.db_type,
                "created_at": kb.created_at.strftime("%Y-%m-%d %H:%M:%S") if kb.created_at else None
            }
        }
    except Exception as e:
        logger.error(f"create_knowledge_base error: {e}")
        db.session.rollback()
        raise


def search_knowledge_base(kb_name: str, query: str, top_k: int = 5) -> List[Dict]:
    """Search knowledge base"""
    try:
        # Get knowledge base
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"Knowledge base does not exist: {kb_name}")

        # Get the vector representation of the query text
        query_embedding = asyncio.run(get_embeddings([query], kb.embedding_model_name))[0]

        # Use Chroma to search
        store = ChromaStore()
        results = store.search(
            kb_name=kb_name,
            query_embedding=query_embedding,
            top_k=top_k
        )

        # Get complete content
        for result in results:
            content_id = result['metadata']['content_id']
            content = JSONContent.query.get(content_id)
            if content:
                result['json_content'] = json.loads(content.content)

        return results

    except Exception as e:
        logger.error(f"search_knowledge_base error: {e}")
        raise


def upload_json_file(kb_name: str, file) -> Dict:
    """Upload JSON file"""
    try:
        # Read JSON file
        json_items = json.load(file)
        if not isinstance(json_items, list):
            raise ValueError("JSON content must be an array format")

        # Securely process file name
        filename = secure_filename_with_unicode(file.filename)

        # Build file save path
        save_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], kb_name)
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, filename)

        # Save file
        file.save(file_path)

        return json_items

    except Exception as e:
        logger.error(f"Upload JSON file failed: {str(e)}")
        raise


def get_json_items(kb_name: str, page: int = 1, page_size: int = 10, all_item: bool = False) -> Dict:
    """Get JSON records"""
    try:
        # Get knowledge base
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"Knowledge base does not exist: {kb_name}")

        # Build query
        query = JSONContent.query.filter_by(knowledge_base_id=kb.id)

        # Get total
        total = query.count()
        if all_item:
            return query.all()

        # Ensure page number and page size are integers
        try:
            page = int(page)
            page_size = int(page_size)
        except (TypeError, ValueError):
            page = 1
            page_size = 10

        # Pagination
        pagination = query.order_by(JSONContent.created_at.desc()).paginate(
            page=page,
            per_page=page_size,
            error_out=False
        )

        items = []
        for item in pagination.items:
            try:
                content = json.loads(item.content) if item.content else {}
                items.append({
                    'id': item.id,
                    'content': content,
                    'vector_id': item.vector_id,
                    'status': item.status,
                    'error_msg': item.error_msg,
                    'created_at': item.created_at.strftime('%Y-%m-%d %H:%M:%S') if item.created_at else None
                })
            except json.JSONDecodeError:
                logger.error(f"JSON parsing failed, content_id: {item.id}")
                continue

        return {
            'total': total,
            'items': items
        }
    except Exception as e:
        logger.error(f"Get JSON records failed: {str(e)}")
        return {
            'total': 0,
            'items': []
        }


def secure_filename_with_unicode(filename: str) -> str:
    """Handle filenames containing Unicode characters"""
    # Separate filename and extension
    name, ext = os.path.splitext(filename)

    # Process file name (keep Unicode characters such as Chinese)
    name = "".join(c for c in name if c.isalnum() or c.isspace() or c in '-._')
    name = name.strip('._')

    # If filename is empty, use timestamp
    if not name:
        name = str(int(time.time()))

    return name + ext


def add_kb_items(kb_name: str, items: List[Dict]) -> Dict:
    """Add knowledge base items (without vectorization)"""
    try:
        # Get knowledge base
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"Knowledge base does not exist: {kb_name}")


        # Create content records
        contents = []

        for item in items:
            # Validate data format
            if not isinstance(item, dict):
                raise ValueError("Data item must be a dictionary type")
            # Validate if has keyword, detail, description
            if 'keyword' not in item.keys():
                raise ValueError("Data item must contain keyword field")
            
            if 'detail' not in item.keys():
                raise ValueError("Data item must contain detail field")

            if 'description' not in item.keys():
                raise ValueError("Data item must contain description field")

            if 'type' not in item.keys():
                raise ValueError("Data item must contain type field")

            if 'tree' not in item.keys():
                raise ValueError("Data item must contain tree field")
            
            # Get and verify embedding text keyword--separator--detail description
            embedding_text = f"{item.get('keyword')}--separator--{item.get('detail')}{item.get('description')}"

            # Calculate content hash
            content_str = json.dumps(item, sort_keys=True)
            content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()

            # Create content object
            content = JSONContent(
                knowledge_base_id=kb.id,
                content=content_str,
                content_type=item.get('type'),
                content_hash=content_hash,
                embedding_text=embedding_text,
                token_count=len(tiktoken.get_encoding("cl100k_base").encode(embedding_text)),
                status="pending"  # Explicitly set initial status
            )
            contents.append(content)

        # If there is no valid data
        if not contents:
            return {
                'status': False,
                'message': 'No valid data items found'
            }

        try:
            db.session.add_all(contents)
            db.session.commit()

            return {
                'status': True,
                'message': f'Successfully added {len(contents)} records',
                'data': {
                    'success_ids': [c.id for c in contents]
                }
            }
        except Exception as e:
            db.session.rollback()
            logger.error(f"Save content records failed: {str(e)}")
            raise

    except Exception as e:
        logger.error(f"Add knowledge base items failed: {str(e)}")
        return {
            'status': False,
            'message': f'Add failed: {str(e)}'
        }


def delete_kb_items(kb_name: str, item_ids: List[int] = None) -> Dict:
    """Delete knowledge base items
    
    Args:
        kb_name: Knowledge base name
        item_ids: List of item IDs to delete, if None, delete all items
    """
    try:
        # Get knowledge base
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"Knowledge base does not exist: {kb_name}")

        # Build query
        query = JSONContent.query.filter_by(knowledge_base_id=kb.id)
        if item_ids:
            query = query.filter(JSONContent.id.in_(item_ids))

        # Get content to delete
        contents = query.all()
        if not contents:
            return {
                'status': True,
                'message': 'No items found to delete'
            }

        # Get vector_ids
        vector_type_ids = {}
        for content in contents:
            if content.content_type not in vector_type_ids:
                vector_type_ids[content.content_type] = []
            vector_type_ids[content.content_type].append(content.vector_id)

        try:
            # Delete vectors from Chroma
            if vector_type_ids:
                store = ChromaStore()
                for content_type, vector_ids in vector_type_ids.items():
                    store.delete_by_ids(kb.kb_name, content_type, vector_ids)

            # Delete records from database
            for content in contents:
                db.session.delete(content)
            db.session.commit()

            return {
                'status': True,
                'message': f'Successfully deleted {len(contents)} records'
            }

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Delete failed: {str(e)}")

    except Exception as e:
        logger.error(f"delete_kb_items error: {str(e)}")
        raise


def update_knowledge_base(kb_id: int, data: Dict) -> Dict:
    """Update knowledge base"""
    try:
        kb = KnowledgeBase.query.filter_by(id=kb_id).first()
        if not kb:
            return {
                "status": False,
                "msg": f"Knowledge base does not exist"
            }

        # Update knowledge base information
        if 'kb_info' in data:
            kb.kb_info = data['kb_info']
        if 'kb_name' in data:
            kb.kb_name = data['kb_name']

        db.session.commit()

        return {
            "status": True,
            "data": get_knowledge_base(kb.kb_name)
        }
    except Exception as e:
        logger.error(f"update_knowledge_base error: {e}")
        db.session.rollback()
        raise


def delete_knowledge_base(kb_name: str) -> Dict:
    """Delete knowledge base and all associated data
    
    Args:
        kb_name: Knowledge base name
        
    Returns:
        Dict: Delete result
    """
    try:
        # Get knowledge base
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            return {
                "status": False,
                "msg": f"Knowledge base '{kb_name}' does not exist"
            }

        try:
            # 1. Delete all JSON content records
            JSONContent.query.filter_by(knowledge_base_id=kb.id).delete()

            # 2. Delete Chroma collection (will automatically delete all vectors in the collection)
            store = ChromaStore()
            store.delete_collection(kb.kb_name)

        except Exception as e:
            logger.error(f"Delete associated data failed: {str(e)}")
            db.session.rollback()
            return {
                "status": False,
                "msg": f"Delete associated data failed: {str(e)}"
            }

        # 3. Delete knowledge base itself
        db.session.delete(kb)
        db.session.commit()

        return {
            "status": True,
            "data": {
                "kb_name": kb_name,
                "message": "Knowledge base deleted successfully"
            }
        }
    except Exception as e:
        logger.error(f"delete_knowledge_base error: {e}")
        db.session.rollback()
        raise


if __name__ == "__main__":
    get_json_items(kb_name="MySQL")
