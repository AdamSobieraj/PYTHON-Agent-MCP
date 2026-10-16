import json
from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import List, Optional, Dict, Any


@dataclass
class CostMetrics:
    """
    Token usage and cost for one model usage in one system section.

    Sections:
        embedding          - LocalEmbeddingClient (input tokens only)
        chunking_agentic   - LLM calls in NewAgenticStrategy
        agent_generation   - final answer generation (AnalysisAgent)

    Costs (USD) are computed from the COST section in .env
    (COST_INPUT_PER_MTOKEN / COST_OUTPUT_PER_MTOKEN).
    """
    model: str
    section: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost_input: Optional[float] = None
    cost_output: Optional[float] = None
    cost_total: Optional[float] = None
    provider: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> Dict[str, Any]:
        """Converts the model to a dictionary for database storage"""
        return {
            "model": self.model,
            "section": self.section,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "cost_input": self.cost_input,
            "cost_output": self.cost_output,
            "cost_total": self.cost_total,
            "provider": self.provider,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


class RetrievalMetrics:
    """Metrics for the retrieval phase"""
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
    """Metrics for the generation phase"""
    query: str
    answer: str
    context_length: Optional[int] = None
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
    """
    Metrics for the entire RAG pipeline.
    retrieval_id / generation_id: links to existing rows
    (when set, insert_full_metrics does not duplicate them).
    """
    retrieval: RetrievalMetrics
    generation: Optional[GenerationMetrics] = None
    total_latency_ms: Optional[int] = None
    retrieval_id: Optional[int] = None
    generation_id: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "retrieval": self.retrieval.to_dict(),
            "generation": self.generation.to_dict() if self.generation else None,
            "total_latency_ms": self.total_latency_ms,
            "retrieval_id": self.retrieval_id,
            "generation_id": self.generation_id
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class ChunkingRunMetrics:
    """
    Metrics of a single chunking run (experiments E1-E4).
    Scope: identification + configuration (reproducibility)
    + quality (E1) + cost (E2) + time.
    """
    experiment_id: str
    strategy: str
    source: str
    num_chunks: int
    timestamp: str
    category: Optional[str] = None
    # Configuration (reproducibility)
    chunk_size: Optional[int] = None
    chunk_overlap: Optional[int] = None
    batch_size: Optional[int] = None
    force_refresh: Optional[bool] = None
    embedding_model: Optional[str] = None
    llm_model: Optional[str] = None
    python_version: Optional[str] = None
    # Chunking quality (E1)
    avg_chunk_len: Optional[float] = None
    max_chunk_len: Optional[int] = None
    # Standard deviation of chunk lengths (H5/PB6 - length stability)
    std_chunk_len: Optional[float] = None
    empty_chunks: Optional[int] = None
    too_short_chunks: Optional[int] = None
    over_limit_chunks: Optional[int] = None
    over_limit_ratio: Optional[float] = None
    coverage: Optional[float] = None
    coherence: Optional[float] = None
    # Cost (E2)
    embedding_http_requests: Optional[int] = None
    texts_embedded: Optional[int] = None
    llm_calls: Optional[int] = None
    fallbacks: Optional[int] = None
    # Time
    chunking_ms: Optional[float] = None
    embedding_ms: Optional[float] = None
    storage_ms: Optional[float] = None
    total_ms: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class MetricsStats:
    """Aggregated metrics statistics"""
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