# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: vector_db
# @Author: xxxx
# @Time: 2024/9/1 19:29

from tqdm import tqdm
import Stemmer

from langchain_chroma.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# https://huggingface.co/spaces/mteb/leaderboard
# https://stackoverflow.com/questions/76379440/how-to-see-the-embedding-of-the-documents-with-chroma-or-any-other-db-saved-in


class VectorDB:
    def __init__(self, db_id, db_path=None, embed_func=None):
        self.db_id = db_id
        if db_id == "Chroma":
            self.db = Chroma(persist_directory=db_path, embedding_function=embed_func)
            if isinstance(self.db.embeddings, HuggingFaceEmbeddings) \
                    and self.db.embeddings.client.tokenizer.pad_token is None:
                self.db.embeddings.client.tokenizer.pad_token = self.db.embeddings.client.tokenizer.eos_token
        elif db_id == "BM25":
            self.db = embed_func

    def load_vector(self, docs, batch_size=64, top_k=5):
        if self.db_id == "BM25":
            # We can pass in the index, docstore, or list of nodes to create the retriever
            self.db = self.db.from_defaults(
                nodes=docs,
                similarity_top_k=top_k,
                # Optional: We can pass in the stemmer and set the language for stopwords
                # This is important for removing stopwords and stemming the query + text
                # The default is english for both
                stemmer=Stemmer.Stemmer("english"),
                language="english",
            )

        else:
            texts = [doc.page_content for doc in docs]
            metadatas = [doc.metadata for doc in docs]
            ids = [str(i) for i in range(len(docs))]

            self.batch_upsert(texts, metadatas, ids, batch_size)

    def batch_upsert(self, texts, metadatas, ids, batch_size):
        for i in tqdm(range(0, len(texts), batch_size)):
            end = min(i + batch_size, len(texts))
            current_texts = texts[i:end]
            current_metadatas = metadatas[i:end]
            current_ids = ids[i:end]
            self.db.add_texts(current_texts, metadatas=current_metadatas, ids=current_ids)
