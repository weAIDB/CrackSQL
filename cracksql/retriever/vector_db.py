# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: vector_db
# @Author: xxxx
# @Time: 2024/9/1 19:29

from tqdm import tqdm
from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# https://huggingface.co/spaces/mteb/leaderboard
# https://stackoverflow.com/questions/76379440/how-to-see-the-embedding-of-the-documents-with-chroma-or-any-other-db-saved-in


class VectorDB:
    """向量数据库,用于向量检索"""
    
    def __init__(self, db_path, embed_func):
        """初始化向量数据库
        
        Args:
            db_path: 数据库路径
            embed_func: 嵌入函数
        """
        self.db = Chroma(persist_directory=db_path, embedding_function=embed_func)
        if isinstance(self.db.embeddings, HuggingFaceEmbeddings) \
                and self.db.embeddings.client.tokenizer.pad_token is None:
            self.db.embeddings.client.tokenizer.pad_token = self.db.embeddings.client.tokenizer.eos_token

    def load_vector(self, docs, batch_size=64):
        """加载文档向量到数据库
        
        Args:
            docs: 文档列表
            batch_size: 批处理大小
        """
        texts = [doc.page_content for doc in docs]
        metadatas = [doc.metadata for doc in docs]
        ids = [str(i) for i in range(len(docs))]
        self.batch_upsert(texts, metadatas, ids, batch_size)

    def batch_upsert(self, texts, metadatas, ids, batch_size):
        """批量插入/更新文档
        
        Args:
            texts: 文本列表
            metadatas: 元数据列表
            ids: ID列表
            batch_size: 批处理大小
        """
        for i in tqdm(range(0, len(texts), batch_size)):
            end = min(i + batch_size, len(texts))
            current_texts = texts[i:end]
            current_metadatas = metadatas[i:end]
            current_ids = ids[i:end]
            self.db.add_texts(current_texts, metadatas=current_metadatas, ids=current_ids)
