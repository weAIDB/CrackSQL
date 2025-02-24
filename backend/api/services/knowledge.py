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
    """获取知识库列表"""
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
                "user_id": kb.user_id,
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
    """获取单个知识库"""
    try:
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            return None

        return {
            "id": kb.id,
            "kb_name": kb.kb_name,
            "kb_info": kb.kb_info,
            "user_id": kb.user_id,
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


def create_knowledge_base(kb_name: str, user_id: int, kb_info: str, embedding_model_name: str, db_type: str) -> Dict:
    """创建知识库"""
    try:
        # 检查知识库名称是否已存在
        if KnowledgeBase.query.filter_by(kb_name=kb_name).first():
            return {
                "status": False,
                "msg": f"知识库 '{kb_name}' 已存在"
            }

        # 获取 LLMModel 实例
        embedding_model = LLMModel.query.filter_by(
            name=embedding_model_name,
            category='embedding',
            is_active=True
        ).first()

        if not embedding_model:
            return {
                "status": False,
                "msg": "无效的Embedding模型"
            }

        # 创建知识库
        kb = KnowledgeBase(
            kb_name=kb_name,
            user_id=user_id,
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
    """搜索知识库"""
    try:
        # 获取知识库
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"知识库不存在: {kb_name}")

        # 获取查询文本的向量表示
        query_embedding = asyncio.run(get_embeddings([query], kb.embedding_model_name))[0]

        # 使用Chroma搜索
        store = ChromaStore()
        results = store.search(
            kb_name=kb_name,
            query_embedding=query_embedding,
            top_k=top_k
        )

        # 获取完整内容
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
    """上传JSON文件"""
    try:
        # 读取JSON文件
        json_items = json.load(file)
        if not isinstance(json_items, list):
            raise ValueError("JSON内容必须是数组格式")

        # 安全处理文件名
        filename = secure_filename_with_unicode(file.filename)

        # 构建文件保存路径
        save_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], kb_name)
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, filename)

        # 保存文件
        file.save(file_path)

        return json_items

    except Exception as e:
        logger.error(f"上传JSON文件失败: {str(e)}")
        raise


def get_json_items(kb_name: str, page: int = 1, page_size: int = 10) -> Dict:
    """获取JSON记录"""
    try:
        # 获取知识库
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"知识库不存在: {kb_name}")

        # 构建查询
        query = JSONContent.query.filter_by(knowledge_base_id=kb.id)

        # 获取总数
        total = query.count()

        # 确保页码和每页数量是整数
        try:
            page = int(page)
            page_size = int(page_size)
        except (TypeError, ValueError):
            page = 1
            page_size = 10

        # 分页
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
                logger.error(f"JSON解析失败，content_id: {item.id}")
                continue

        return {
            'total': total,
            'items': items
        }
    except Exception as e:
        logger.error(f"获取JSON记录失败: {str(e)}")
        return {
            'total': 0,
            'items': []
        }


def secure_filename_with_unicode(filename: str) -> str:
    """处理包含Unicode字符的文件名"""
    # 分离文件名和扩展名
    name, ext = os.path.splitext(filename)

    # 处理文件名(保留中文等Unicode字符)
    name = "".join(c for c in name if c.isalnum() or c.isspace() or c in '-._')
    name = name.strip('._')

    # 如果文件名为空，使用时间戳
    if not name:
        name = str(int(time.time()))

    return name + ext


def add_kb_items(kb_name: str, items: List[Dict], user_id: int = None) -> Dict:
    """添加知识库条目(不包含向量化)"""
    try:
        # 获取知识库
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"知识库不存在: {kb_name}")


        # 创建内容记录
        contents = []

        for item in items:
            # 验证数据格式
            if not isinstance(item, dict):
                raise ValueError("数据项必须是字典类型")
            # 验证是否有keyword、detail、description
            if 'keyword' not in item.keys():
                raise ValueError("数据项必须包含keyword字段")
            
            if 'detail' not in item.keys():
                raise ValueError("数据项必须包含detail字段")

            if 'description' not in item.keys():
                raise ValueError("数据项必须包含description字段")

            if 'type' not in item.keys():
                raise ValueError("数据项必须包含type字段")

            if 'tree' not in item.keys():
                raise ValueError("数据项必须包含tree字段")
            
            # 获取并验证embedding文本 keyword--separator--detaildescription
            embedding_text = f"{item.get('keyword')}--separator--{item.get('detail')}{item.get('description')}"

            # 计算内容哈希
            content_str = json.dumps(item, sort_keys=True)
            content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()

            # 创建内容对象
            content = JSONContent(
                knowledge_base_id=kb.id,
                user_id=user_id,
                content=content_str,
                content_type=item.get('type'),
                content_hash=content_hash,
                embedding_text=embedding_text,
                token_count=len(tiktoken.get_encoding("cl100k_base").encode(embedding_text)),
                status="pending"  # 显式设置初始状态
            )
            contents.append(content)

        # 如果没有有效数据
        if not contents:
            return {
                'status': False,
                'message': '没有找到有效的数据项'
            }

        try:
            db.session.add_all(contents)
            db.session.commit()

            return {
                'status': True,
                'message': f'成功添加 {len(contents)} 条记录',
                'data': {
                    'success_ids': [c.id for c in contents]
                }
            }
        except Exception as e:
            db.session.rollback()
            logger.error(f"保存内容记录失败: {str(e)}")
            raise

    except Exception as e:
        logger.error(f"添加知识库条目失败: {str(e)}")
        return {
            'status': False,
            'message': f'添加失败: {str(e)}'
        }


def delete_kb_items(kb_name: str, item_ids: List[int] = None) -> Dict:
    """删除知识库条目
    
    Args:
        kb_name: 知识库名称
        item_ids: 要删除的条目ID列表，如果为None则删除所有条目
    """
    try:
        # 获取知识库
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            raise ValueError(f"知识库不存在: {kb_name}")

        # 构建查询
        query = JSONContent.query.filter_by(knowledge_base_id=kb.id)
        if item_ids:
            query = query.filter(JSONContent.id.in_(item_ids))

        # 获取要删除的内容
        contents = query.all()
        if not contents:
            return {
                'status': True,
                'message': '没有找到要删除的条目'
            }

        # 获取vector_ids
        vector_type_ids = {}
        for content in contents:
            if content.content_type not in vector_type_ids:
                vector_type_ids[content.content_type] = []
            vector_type_ids[content.content_type].append(content.vector_id)

        try:
            # 从Chroma中删除向量
            if vector_type_ids:
                store = ChromaStore()
                for content_type, vector_ids in vector_type_ids.items():
                    store.delete_by_ids(kb.kb_name, content_type, vector_ids)

            # 从数据库中删除记录
            for content in contents:
                db.session.delete(content)
            db.session.commit()

            return {
                'status': True,
                'message': f'成功删除 {len(contents)} 条记录'
            }

        except Exception as e:
            db.session.rollback()
            raise Exception(f"删除失败: {str(e)}")

    except Exception as e:
        logger.error(f"delete_kb_items error: {str(e)}")
        raise


def update_knowledge_base(kb_id: int, data: Dict) -> Dict:
    """更新知识库"""
    try:
        kb = KnowledgeBase.query.filter_by(id=kb_id).first()
        if not kb:
            return {
                "status": False,
                "msg": f"知识库不存在"
            }

        # 更新知识库信息
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
    """删除知识库及其所有关联数据
    
    Args:
        kb_name: 知识库名称
        
    Returns:
        Dict: 删除结果
    """
    try:
        # 获取知识库
        kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
        if not kb:
            return {
                "status": False,
                "msg": f"知识库 '{kb_name}' 不存在"
            }

        try:
            # 1. 删除所有JSON内容记录c
            JSONContent.query.filter_by(knowledge_base_id=kb.id).delete()

            # 2. 删除Chroma集合（会自动删除集合中的所有向量）
            store = ChromaStore()
            store.delete_collection(kb.kb_name)

        except Exception as e:
            logger.error(f"删除关联数据失败: {str(e)}")
            db.session.rollback()
            return {
                "status": False,
                "msg": f"删除关联数据失败: {str(e)}"
            }

        # 3. 最后删除知识库本身
        db.session.delete(kb)
        db.session.commit()

        return {
            "status": True,
            "data": {
                "kb_name": kb_name,
                "message": "知识库删除成功"
            }
        }
    except Exception as e:
        logger.error(f"delete_knowledge_base error: {e}")
        db.session.rollback()
        raise
