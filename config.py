from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

class IngestionConfig(BaseModel):
    source_type: Literal["web", "file_upload", "api"] = "file_upload"
    supported_formats: List[str] = Field(default_factory=lambda: ["pdf", "docx", "xlsx", "csv", "txt", "md"])
    max_depth: Optional[int] = None
    use_ocr: bool = False
    clean_text: bool = True

class ChunkingConfig(BaseModel):
    strategy: Literal["fixed_size", "recursive", "semantic", "markdown"] = "recursive"
    chunk_size: int = 512
    chunk_overlap: int = 50
    separator_priority: List[str] = Field(default_factory=lambda: ["\n\n", "\n", " ", ""])

class EmbeddingConfig(BaseModel):
    model: str = "multilingual-e5-large"
    dimensions: int = 1024
    batch_size: int = 32

class VDBConfig(BaseModel):
    provider: Literal["elasticsearch", "qdrant", "pgvector", "milvus"] = "qdrant"
    collection_name: str = "default_namespace"
    similarity_metric: Literal["cosine", "dot", "euclidean"] = "cosine"
    m: int = 16
    ef_construction: int = 100
    ef_search: int = 64

class RetrievalConfig(BaseModel):
    search_mode: Literal["vector", "keyword", "hybrid"] = "hybrid"
    alpha: float = 0.5
    top_k: int = 10
    score_threshold: float = 0.7
    use_reranker: bool = True
    rerank_top_n: int = 3
    parent_child_retrieval: bool = False

class LLMConfig(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4o"
    context_window: int = 8192
    temperature: float = 0.7
    top_p: float = 0.9
    max_tokens: int = 1024
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    stop_sequences: List[str] = Field(default_factory=list)
    system_prompt_template: str = "You are a helpful assistant. Context: {{context}}"
    citation_mode: Literal["inline", "json", "none"] = "inline"

class MemoryConfig(BaseModel):
    strategy: Literal["buffer", "summary", "stateless"] = "buffer"
    window_size: int = 5
    query_rewriting: bool = True

class RAGPipelineConfig(BaseModel):
    ingestion: IngestionConfig = Field(default_factory=IngestionConfig)
    chunking: ChunkingConfig = Field(default_factory=ChunkingConfig)
    embedding: EmbeddingConfig = Field(default_factory=EmbeddingConfig)
    vdb: VDBConfig = Field(default_factory=VDBConfig)
    retrieval: RetrievalConfig = Field(default_factory=RetrievalConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    memory: MemoryConfig = Field(default_factory=MemoryConfig)
