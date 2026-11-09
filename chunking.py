from typing import List
from config import ChunkingConfig
from ingestion import Document

class Chunker:
    def __init__(self, config: ChunkingConfig):
        self.config = config

    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        print(f"Chunking documents using {self.config.strategy} strategy...")
        chunked_docs = []
        for doc in documents:
            # Mock chunking logic
            chunked_docs.append(Document(
                content=f"Chunk 1 of: {doc.content[:10]}...",
                metadata=doc.metadata.copy()
            ))
        return chunked_docs
