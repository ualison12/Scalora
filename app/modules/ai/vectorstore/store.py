from abc import ABC, abstractmethod
from typing import List, Dict, Any

class VectorStore(ABC):
    @abstractmethod
    async def add_vectors(self, vectors: List[List[float]], documents: List[Dict[str, Any]]) -> None:
        pass

    @abstractmethod
    async def similarity_search(self, query_vector: List[float], k: int = 4) -> List[Dict[str, Any]]:
        pass
