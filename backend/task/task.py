import asyncio
from config.logging_config import logger
from models import KnowledgeBase, JSONContent
from llm_model.embeddings import get_embeddings
from vector_store.chroma_store import ChromaStore
from config.db_config import db, db_session_manager
import uuid
import json
from typing import List


@db_session_manager
def process_json_data(kb_name: str, item_ids: List[int], user_id: int):
    """处理JSON数据"""

    async def _async_process_json_data():
        try:
            # 获取知识库
            kb = KnowledgeBase.query.filter_by(kb_name=kb_name).first()
            if not kb:
                raise ValueError(f"知识库不存在: {kb_name}")

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
                embedding_type_texts = {}
                for c in contents:
                    if c.content_type not in embedding_type_texts.keys():
                        embedding_type_texts[c.content_type] = {
                            'original_contents': [],
                            'texts': [],
                            'metadatas': []
                        }
                    embedding_type_texts[c.content_type]['original_contents'].append(c)
                    embedding_type_texts[c.content_type]['texts'].append(c.embedding_text)
                    embedding_type_texts[c.content_type]['metadatas'].append({
                        'content_id': str(c.id),
                        'knowledge_base_id': str(kb.id),
                        'content_type': c.content_type,
                        'content': json.dumps(c.content)
                    })


                for embedding_type in embedding_type_texts.keys():

                    texts = embedding_type_texts[embedding_type]['texts']
                    metadatas = embedding_type_texts[embedding_type]['metadatas']
                    embeddings = await get_embeddings(
                        texts,
                        model_name=kb.embedding_model_name
                    )                                    # 使用uuid生成唯一ID
                    vector_ids = [str(uuid.uuid4()) for _ in texts]
                    original_contents = embedding_type_texts[embedding_type]['original_contents']
                    # 保存到Chroma
                    store = ChromaStore()
                    store.add_texts(
                        kb_name=kb.kb_name,
                        content_type=embedding_type,
                        texts=texts,
                        embeddings=embeddings,
                        ids=vector_ids,
                        metadatas=metadatas
                    )

                    # 更新状态
                    for original_content, vector_id in zip(original_contents, vector_ids):
                        original_content.status = 'completed'
                        original_content.vector_id = vector_id
                        original_content.error_msg = ""

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
