import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any


@dataclass
class RetrievalMetrics:
    """Metryki dla fazy retrieval"""
    query: str
    collection_name: str
    num_results: int
    top_scores: List[float]
    avg_score: float
    latency_ms: int
    timestamp: str
    embedding_latency_ms: Optional[int] = None
    search_latency_ms: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class GenerationMetrics:
    """Metryki dla fazy generation"""
    query: str
    answer: str
    context_length: int
    tokens_used: Optional[int] = None
    latency_ms: Optional[int] = None
    cost: Optional[float] = None
    timestamp: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class FullRAGMetrics:
    """Metryki dla całego pipeline RAG"""
    retrieval: RetrievalMetrics
    generation: Optional[GenerationMetrics] = None
    total_latency_ms: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "retrieval": self.retrieval.to_dict(),
            "generation": self.generation.to_dict() if self.generation else None,
            "total_latency_ms": self.total_latency_ms
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class MetricsStats:
    """Zagregowane statystyki metryk"""
    total_queries: int
    avg_latency_ms: float
    p50_latency_ms: float
    p95_latency_ms: float
    p99_latency_ms: float
    avg_score: float
    avg_results: float
    queries_no_results: int
    per_collection: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)