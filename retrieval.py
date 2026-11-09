from typing import List
from config import RetrievalConfig
from ingestion import Document
from embedding import BaseVDB, BaseEmbedder

class Retriever:
    def __init__(self, config: RetrievalConfig, vdb: BaseVDB, embedder: BaseEmbedder):
        self.config = config
        self.vdb = vdb
        self.embedder = embedder

    def retrieve(self, query: str) -> List[Document]:
        print(f"Retrieving documents using {self.config.search_mode} search mode...")
        query_embedding = self.embedder.embed_query(query)
        results = self.vdb.search(query_embedding, top_k=self.config.top_k)

        if self.config.use_reranker:
            print(f"Reranking top {self.config.rerank_top_n} results...")
            results = results[:self.config.rerank_top_n]

        return results
