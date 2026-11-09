from dataclasses import dataclass
from typing import List, Dict, Any
from config import IngestionConfig

@dataclass
class Document:
    content: str
    metadata: Dict[str, Any]

class BaseIngestor:
    def __init__(self, config: IngestionConfig):
        self.config = config

    def ingest(self, source: Any) -> List[Document]:
        print(f"Ingesting from {source} using {self.config.source_type}...")
        # Mock ingestion
        return [Document(content="Sample document content.", metadata={"source": str(source)})]
