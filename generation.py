from typing import List
from config import LLMConfig
from ingestion import Document

class Generator:
    def __init__(self, config: LLMConfig):
        self.config = config

    def generate(self, query: str, context_docs: List[Document], chat_history: List[str]) -> str:
        print(f"Generating response using {self.config.provider} ({self.config.model})...")
        context_str = "\n".join([doc.content for doc in context_docs])
        return f"Mock response to: '{query}' based on context: '{context_str}'"
