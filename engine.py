from config import RAGPipelineConfig
from ingestion import BaseIngestor, Document
from chunking import Chunker
from embedding import BaseEmbedder, BaseVDB
from retrieval import Retriever
from generation import Generator
from memory import MemoryManager
from typing import List, Any

class RAGEngine:
    def __init__(self, config: RAGPipelineConfig):
        self.config = config

        # Initialize modules for the 6 phases
        self.ingestor = BaseIngestor(config.ingestion)
        self.chunker = Chunker(config.chunking)
        self.embedder = BaseEmbedder(config.embedding)
        self.vdb = BaseVDB(config.vdb)
        self.retriever = Retriever(config.retrieval, self.vdb, self.embedder)
        self.generator = Generator(config.llm)
        self.memory = MemoryManager(config.memory)

    def ingest_documents(self, source: Any) -> None:
        """Pipeline phase 1-3: Ingest, Chunk, Embed, and Index."""
        print("\n--- Starting Ingestion Pipeline ---")
        docs = self.ingestor.ingest(source)
        chunked_docs = self.chunker.chunk_documents(docs)
        embeddings = self.embedder.embed_documents(chunked_docs)
        self.vdb.insert(chunked_docs, embeddings)
        print("--- Ingestion Pipeline Complete ---\n")

    def run_query(self, query: str) -> str:
        """Pipeline phase 4-6: Retrieve, Generate, and Manage Memory."""
        print(f"--- Processing Query: '{query}' ---")

        # Memory/Query rewriting
        processed_query = self.memory.rewrite_query(query)

        # Retrieval
        retrieved_docs = self.retriever.retrieve(processed_query)

        # Generation
        history = self.memory.get_history()
        response = self.generator.generate(processed_query, retrieved_docs, history)

        # Update Memory
        self.memory.add_interaction(query, response)

        print("--- Query Processing Complete ---\n")
        return response
