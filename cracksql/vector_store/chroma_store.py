import os
import re
import hashlib
import chromadb
from chromadb.config import Settings
from typing import List, Dict, Optional

from cracksql.config.logging_config import logger
from chromadb.api.models.Collection import Collection
from cracksql.api.utils.retry import retry_on_error


def convert_distance_to_score(distance: float) -> float:
    """
    Convert Chroma's distance value to a similarity score of 0-100
    Chroma uses cosine distance (1 - cosine_similarity)
    distance = 0 means completely identical, distance = 2 means completely opposite
    We convert it to: 0 means completely different, 100 means completely identical
    """

    if distance is None:
        return 0
    # Map distance from [0,2] to [0,100]
    score = (1 - distance / 2) * 100
    # Round to two decimal places
    score = round(score, 2)
    # Ensure score is within 0-100 range
    return max(0, min(100, score))


def generate_collection_id(kb_name: str, content_type: str) -> str:
    """Generate collection ID
    Args:
        kb_name: Knowledge base name
        content_type: Content type
        
    Returns:
        str: Valid table name
    """
    # Use MD5 to hash Chinese names, ensuring table name uniqueness
    name_hash = hashlib.md5(kb_name.encode('utf-8')).hexdigest()[:8]
    # Remove all non-alphanumeric characters, convert to lowercase
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', kb_name.encode('ascii', 'ignore').decode('ascii').lower())
    # Combine table name: prefix + safe_name + hash
    return f"vector_store_{safe_name}_{name_hash}_{content_type}"


class ChromaStore:
    """Chroma vector storage manager"""

    def __init__(self, persist_directory: str = "./instance/chroma"):
        """
        Initialize ChromaStore
        
        Args:
            persist_directory: Persistence directory
        """
        self.persist_directory = persist_directory
        os.makedirs(persist_directory, exist_ok=True)

        # Configure Chroma client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                anonymized_telemetry=False,  # Disable telemetry
                allow_reset=True,
                is_persistent=True
            )
        )

    def _get_collection(self, collection_id: str):
        """Get collection"""
        try:
            return self.client.get_collection(
                name=collection_id,
                embedding_function=None
            )
        except Exception as e:
            logger.error(f"Failed to get collection: {str(e)}")
            return None

    @retry_on_error(logger_name="ChromaDB")
    def get_or_create_collection(self, collection_id: str, dimension: int = 1536) -> Collection:
        """Get or create collection
        
        Args:
            collection_id: Collection ID
            dimension: Vector dimension
            
        Returns:
            str: Collection ID
        """
        try:
            # First try to get existing collection
            try:
                collection = self.client.get_collection(
                    name=collection_id,
                    embedding_function=None
                )
                logger.info(f"Retrieved existing collection: {collection_id}")
                return collection
            except Exception:
                # If collection doesn't exist, create a new one
                metadata = {
                    "hnsw:space": "cosine",
                    "dimension": str(dimension),
                    "hnsw:search_ef": 200,
                    "hnsw:construction_ef": 200,
                    "hnsw:M": 32
                }

                collection = self.client.create_collection(
                    name=collection_id,
                    embedding_function=None,
                    metadata=metadata
                )
                logger.info(f"Created new collection: {collection_id}")

                return collection
        except Exception as e:
            logger.error(f"Failed to create collection: {str(e)}")
            raise

    def _validate_inputs(self, texts: List[str], embeddings: List[List[float]], ids: Optional[List[str]] = None):
        """Validate input data consistency"""
        if len(texts) != len(embeddings):
            raise ValueError("Number of texts does not match number of vectors")
        if ids and len(ids) != len(texts):
            raise ValueError("Number of IDs does not match number of texts")

    @retry_on_error(logger_name="ChromaDB")
    def add_texts(
            self,
            kb_name: str,
            content_type: str,
            texts: List[str],
            embeddings: List[List[float]],
            metadatas: Optional[List[Dict]] = None,
            ids: Optional[List[str]] = None,
            batch_size: int = 100
    ):
        """Add texts to vector database"""
        self._validate_inputs(texts, embeddings, ids)
        collection_id = generate_collection_id(kb_name, content_type)
        collection = self.get_or_create_collection(collection_id)

        if not ids:
            existing_count = collection.count()
            ids = [str(i) for i in range(existing_count, existing_count + len(texts))]

        # Add in batches to avoid memory overflow
        for i in range(0, len(texts), batch_size):
            end_idx = min(i + batch_size, len(texts))
            collection.add(
                embeddings=embeddings[i:end_idx],
                documents=texts[i:end_idx],
                metadatas=metadatas[i:end_idx] if metadatas else None,
                ids=ids[i:end_idx]
            )

    @retry_on_error(logger_name="ChromaDB")
    def search(
            self,
            kb_name: str,
            query_embedding: List[float],
            content_type: str = None,
            top_k: int = 5,
            where: Optional[Dict] = None,
            where_document: Optional[Dict] = None,
            **kwargs
    ) -> List[Dict]:
        """Search by knowledge base name and content type"""

        collection_ids = []

        if not content_type:
            # Get all content types
            content_types = ['function', 'keyword', 'type', 'operator']
            for content_type in content_types:
                collection_ids.append(generate_collection_id(kb_name, content_type))
        else:
            collection_ids.append(generate_collection_id(kb_name, content_type))

        results_all = []
        for collection_id in collection_ids:
            collection = self._get_collection(collection_id)
            if not collection:
                continue
            try:
                results = collection.query(
                    query_embeddings=[query_embedding],
                    n_results=top_k,
                    where=where,
                    include=["documents", "metadatas", "distances"],
                    where_document=where_document,
                    **kwargs
                )
                results_all.extend([
                    {
                        'content': doc,
                        'metadata': meta if meta else {},
                        'score': convert_distance_to_score(distance),
                        'id': id_
                    }
                    for doc, meta, distance, id_ in zip(
                        results['documents'][0],
                        results['metadatas'][0] if results['metadatas'] else [None] * len(results['documents'][0]),
                        results['distances'][0] if results['distances'] else [None] * len(results['documents'][0]),
                        results['ids'][0]
                    )
                ])
            except Exception as e:
                logger.error(f"Search failed: {str(e)}")
                raise

        # Sort by score
        results_all.sort(key=lambda x: x['score'], reverse=True)

        return results_all

    @retry_on_error(logger_name="ChromaDB")
    def delete_by_ids(self, kb_name: str, content_type: str, ids: List[str]):
        """Delete vectors by ID"""
        collection_id = generate_collection_id(kb_name, content_type)
        collection = self._get_collection(collection_id)
        if not collection:
            return
        try:
            collection.delete(ids=ids)
        except Exception as e:
            logger.error(f"Failed to delete vectors: {str(e)}")
            raise

    @retry_on_error(logger_name="ChromaDB")
    def delete_collection(self, kb_name: str):
        """Delete collection"""
        try:
            for content_type in ['function', 'keyword', 'type', 'operator']:
                self.client.delete_collection(generate_collection_id(kb_name, content_type))
        except Exception as e:
            logger.error(f"Failed to delete collection: {str(e)}")
