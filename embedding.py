from typing import List, Any
from config import EmbeddingConfig, VDBConfig
from ingestion import Document

class BaseEmbedder:
    def __init__(self, config: EmbeddingConfig):
        self.config = config

    def embed_documents(self, documents: List[Document]) -> List[Any]:
        print(f"Embedding documents using {self.config.model}...")
        # Mock embeddings
        return [[0.1] * self.config.dimensions for _ in documents]

    def embed_query(self, query: str) -> Any:
        # Mock single embedding
        return [0.1] * self.config.dimensions

class BaseVDB:
    def __init__(self, config: VDBConfig):
        self.config = config

    def insert(self, documents: List[Document], embeddings: List[Any]):
        print(f"Inserting {len(documents)} docs into {self.config.provider} VDB...")

    def search(self, query_embedding: Any, top_k: int) -> List[Document]:
        print(f"Searching VDB for top {top_k} results...")
        return [Document(content="Retrieved mock content", metadata={"score": 0.95})]
