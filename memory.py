from typing import List, Tuple
from config import MemoryConfig

class MemoryManager:
    def __init__(self, config: MemoryConfig):
        self.config = config
        self.history: List[Tuple[str, str]] = []

    def add_interaction(self, query: str, response: str):
        self.history.append((query, response))
        if self.config.strategy == "buffer" and len(self.history) > self.config.window_size:
            self.history.pop(0)

    def get_history(self) -> List[str]:
        # Formats history as a list of strings
        return [f"User: {q}\nAssistant: {r}" for q, r in self.history]

    def rewrite_query(self, query: str) -> str:
        if self.config.query_rewriting and self.history:
            print(f"Rewriting query based on history...")
            return f"{query} (rewritten)"
        return query
