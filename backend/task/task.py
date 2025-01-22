import asyncio
import json
import tiktoken
from config.logging_config import logger
from models import KnowledgeBase, JSONContent
from llm_model.embeddings import get_embeddings
from vector_store.chroma_store import ChromaStore
import hashlib
from config.db_config import db
import uuid

def process_json_data(kb_name: str, json_items: list, user_id: int = None):
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

                # 创建内容记录
                contents = []
                failed_contents = []  # 记录失败的内容

                for item in json_items:
                    if not isinstance(item, dict):
                        continue

                        
                    # 计算内容哈希
                    content_str = json.dumps(item, sort_keys=True)
                    content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()
                    
                    # 获取embedding文本
                    embedding_text = item.get(kb.embedding_key)

                    # 创建内容对象
                    content = JSONContent(
                        knowledge_base_id=kb.id,
                        user_id=user_id,
                        content=content_str,
                        content_hash=content_hash,
                        token_count=0,  # 初始化为0
                        status="pending"  # 显式设置初始状态
                    )
                    
                    # 检查embedding_text是否存在
                    if embedding_text is None:
                        content.status = "failed"
                        content.error_msg = f"未找到embedding_key '{kb.embedding_key}' 对应的值"
                        failed_contents.append(content)
                        continue
                        
                    # 转换为字符串并检查是否为空
                    embedding_text = str(embedding_text)
                    if not embedding_text.strip():
                        content.status = "failed"
                        content.error_msg = f"embedding_key '{kb.embedding_key}' 对应的值为空"
                        failed_contents.append(content)
                        continue
                    
                    content.embedding_text = embedding_text
                    content.token_count = len(tiktoken.get_encoding("cl100k_base").encode(embedding_text))
                    contents.append(content)
                    
                # 保存所有内容（包括失败的）
                all_contents = contents + failed_contents
                if not all_contents:
                    return {
                        'status': False,
                        'message': '没有找到有效的数据项'
                    }
                
                try:
                    # 使用add_all替代bulk_save_objects
                    db.session.add_all(all_contents)
                    db.session.commit()
                    # commit会自动flush，此时contents中的对象已经有ID
                except Exception as e:
                    db.session.rollback()
                    logger.error(f"保存内容记录失败: {str(e)}")
                    raise

                if not contents:  # 如果没有成功的内容
                    return {
                        'status': False,
                        'message': f'处理完成，所有数据项处理失败: {len(failed_contents)}'
                    }

                try:
                    # 生成向量
                    embedding_texts = [c.embedding_text for c in contents]
                    embeddings = await get_embeddings(
                        embedding_texts,
                        model_name=kb.embedding_model_name
                    )
                    
                    # 使用uuid生成唯一ID
                    vector_ids = [
                        str(uuid.uuid4())
                        for c in contents
                    ]
                    
                    # 准备元数据，确保所有值都是基本类型
                    metadatas = []
                    for c in contents:
                        metadata = {
                            'content_id': str(c.id),
                            'knowledge_base_id': str(kb.id),
                        }
                        metadatas.append(metadata)
                    
                    # 保存到Chroma
                    store = ChromaStore()

                    print("==========metadatas==========:", metadatas)
                    print("==========embedding_texts==========:", embedding_texts)
                    print("==========embeddings==========:", embeddings)
                    print("==========vector_ids==========:", vector_ids)

                    store.add_texts(
                        collection_id=kb.collection_id,
                        texts=embedding_texts,
                        embeddings=embeddings,
                        ids=vector_ids,
                        metadatas=metadatas
                    )
                    
                    # 更新状态 - 直接更新内存中的对象
                    for content, vector_id in zip(contents, vector_ids):
                        content.status = 'completed'
                        content.vector_id = vector_id
                        print(f"执行成功，content_id: {content.id}")
                        
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    logger.error(f"向量化处理失败: {str(e)}")
                    # 更新失败状态 - 直接更新内存中的对象
                    for content in contents:
                        content.status = 'failed'
                        content.error_msg = f"向量化处理失败: {str(e)}"
                    db.session.commit()
                    
                    return {
                        'status': False,
                        'message': f'向量化处理失败: {str(e)}'
                    }

                return {
                    'status': True,
                    'message': f'处理完成，成功: {len(contents)}, 失败: {len(failed_contents)}'
                }
        except Exception as e:
            logger.error(f"处理JSON数据失败: {str(e)}")
            return {
                'status': False,
                'message': f'处理失败: {str(e)}'
            }

    # 运行异步函数
    return asyncio.run(_async_process_json_data())