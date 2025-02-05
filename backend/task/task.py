import asyncio
from config.logging_config import logger
from models import KnowledgeBase, JSONContent
from llm_model.embeddings import get_embeddings
from vector_store.chroma_store import ChromaStore
from config.db_config import db
import uuid
from typing import List

def process_json_data(kb_name: str, item_ids: List[int], user_id: int):
    """处理JSON数据"""

    async def _async_process_json_data():
        try:
            # 在应用上下文中执行数据库操作
            with db.app.app_context():
                # 获取知识库
                kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
                if not kb:
                    raise ValueError(f"知识库不存在: {kb_name}")

                if not kb.embedding_key:
                    raise ValueError(f"知识库未设置embedding_key: {kb_name}")

                # 获取要处理的内容
                contents = JSONContent.query.filter(
                    JSONContent.user_id == user_id,
                    JSONContent.knowledge_base_id == kb.id,
                    JSONContent.id.in_(item_ids)
                ).all()

                if not contents:
                    return {
                        'status': False,
                        'message': '没有找到需要处理的内容'
                    }

                try:
                    # 生成向量
                    embedding_texts = [c.embedding_text for c in contents]
                    embeddings = await get_embeddings(
                        embedding_texts,
                        model_name=kb.embedding_model_name
                    )
                    
                    # 使用uuid生成唯一ID
                    vector_ids = [str(uuid.uuid4()) for _ in contents]
                    
                    # 准备元数据
                    metadatas = []
                    for c in contents:
                        metadata = {
                            'content_id': str(c.id),
                            'knowledge_base_id': str(kb.id),
                        }
                        metadatas.append(metadata)
                    
                    # 保存到Chroma
                    store = ChromaStore()
                    store.add_texts(
                        collection_id=kb.collection_id,
                        texts=embedding_texts,
                        embeddings=embeddings,
                        ids=vector_ids,
                        metadatas=metadatas
                    )
                    
                    # 更新状态
                    for content, vector_id in zip(contents, vector_ids):
                        content.status = 'completed'
                        content.vector_id = vector_id
                        
                    db.session.commit()

                    return {
                        'status': True,
                        'message': f'处理完成，成功: {len(contents)} 条记录'
                    }

                except Exception as e:
                    db.session.rollback()
                    logger.error(f"向量化处理失败: {str(e)}")
                    # 更新失败状态
                    for content in contents:
                        content.status = 'failed'
                        content.error_msg = f"向量化处理失败: {str(e)}"
                    db.session.commit()
                    
                    return {
                        'status': False,
                        'message': f'向量化处理失败: {str(e)}'
                    }

        except Exception as e:
            logger.error(f"处理JSON数据失败: {str(e)}")
            return {
                'status': False,
                'message': f'处理失败: {str(e)}'
            }

    # 运行异步函数
    return asyncio.run(_async_process_json_data())