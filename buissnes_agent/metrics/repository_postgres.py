import os
import logging
import psycopg2
from psycopg2 import pool, Error
from psycopg2.extras import RealDictCursor
from typing import Optional, List, Dict, Any
from contextlib import contextmanager

from .repository_interface import IMetricsRepository
from .models import (
    RetrievalMetrics,
    GenerationMetrics,
    FullRAGMetrics,
    ChunkingRunMetrics,
    MetricsStats
)

logger = logging.getLogger(__name__)


class PostgresConfig:
    """PostgreSQL configuration from ENV"""

    @staticmethod
    def get_connection_params() -> Dict[str, Any]:
        return {
            "host": os.getenv("METRICS_DB_HOST", "localhost"),
            "port": int(os.getenv("METRICS_DB_PORT", "5432")),
            "database": os.getenv("METRICS_DB_NAME", "rag_metrics"),
            "user": os.getenv("METRICS_DB_USER", "postgres"),
            "password": os.getenv("METRICS_DB_PASSWORD", ""),
        }

    @staticmethod
    def get_pool_config() -> Dict[str, int]:
        return {
            "minconn": int(os.getenv("METRICS_DB_POOL_MIN", "1")),
            "maxconn": int(os.getenv("METRICS_DB_POOL_MAX", "10"))
        }


POSTGRES_SCHEMA = """
                  -- Tabela główna dla metryk retrieval
                  CREATE TABLE IF NOT EXISTS rag_retrieval_metrics \
                  ( \
                      id \
                      SERIAL \
                      PRIMARY \
                      KEY, \
                      query \
                      TEXT \
                      NOT \
                      NULL, \
                      collection_name \
                      VARCHAR \
                  ( \
                      255 \
                  ) NOT NULL,
                      num_results INTEGER NOT NULL,
                      top_scores FLOAT [] NOT NULL,
                      avg_score FLOAT NOT NULL,
                      latency_ms INTEGER NOT NULL,
                      embedding_latency_ms INTEGER,
                      search_latency_ms INTEGER,
                      timestamp TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  ),
                      created_at TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  )
                      );

                  CREATE INDEX IF NOT EXISTS idx_retrieval_timestamp ON rag_retrieval_metrics(timestamp);
                  CREATE INDEX IF NOT EXISTS idx_retrieval_collection ON rag_retrieval_metrics(collection_name);
                  CREATE INDEX IF NOT EXISTS idx_retrieval_created_at ON rag_retrieval_metrics(created_at);

-- Tabela dla metryk generation
                  CREATE TABLE IF NOT EXISTS rag_generation_metrics \
                  ( \
                      id \
                      SERIAL \
                      PRIMARY \
                      KEY, \
                      retrieval_id \
                      INTEGER \
                      REFERENCES \
                      rag_retrieval_metrics \
                  ( \
                      id \
                  ) ON DELETE CASCADE,
                      query TEXT NOT NULL,
                      answer TEXT,
                      context_length INTEGER,
                      tokens_used INTEGER,
                      latency_ms INTEGER,
                      cost FLOAT,
                      timestamp TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  ),
                      created_at TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  )
                      );

                  CREATE INDEX IF NOT EXISTS idx_generation_timestamp ON rag_generation_metrics(timestamp);

-- Tabela dla pełnych pipeline metrics
                  CREATE TABLE IF NOT EXISTS rag_full_metrics \
                  ( \
                      id \
                      SERIAL \
                      PRIMARY \
                      KEY, \
                      retrieval_id \
                      INTEGER \
                      REFERENCES \
                      rag_retrieval_metrics \
                  ( \
                      id \
                  ) ON DELETE CASCADE,
                      generation_id INTEGER REFERENCES rag_generation_metrics \
                  ( \
                      id \
                  ) \
                    ON DELETE CASCADE,
                      total_latency_ms INTEGER,
                      timestamp TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  ),
                      created_at TIMESTAMP NOT NULL DEFAULT NOW \
                  ( \
                  )
                      );

                  CREATE INDEX IF NOT EXISTS idx_full_timestamp ON rag_full_metrics(timestamp);

-- Tabela dla metryk fragmentacji (eksperymenty E1-E4)
                  CREATE TABLE IF NOT EXISTS rag_chunking_metrics \
                  ( \
                      id SERIAL PRIMARY KEY, \
                      experiment_id VARCHAR(255) NOT NULL, \
                      strategy VARCHAR(64) NOT NULL, \
                      source TEXT, \
                      category VARCHAR(64), \
                      chunk_size INTEGER, \
                      chunk_overlap INTEGER, \
                      batch_size INTEGER, \
                      force_refresh BOOLEAN, \
                      embedding_model VARCHAR(255), \
                      llm_model VARCHAR(255), \
                      python_version VARCHAR(32), \
                      num_chunks INTEGER NOT NULL, \
                      avg_chunk_len FLOAT, \
                      max_chunk_len INTEGER, \
                      empty_chunks INTEGER, \
                      too_short_chunks INTEGER, \
                      over_limit_chunks INTEGER, \
                      over_limit_ratio FLOAT, \
                      coverage FLOAT, \
                      coherence FLOAT, \
                      embedding_http_requests INTEGER, \
                      texts_embedded INTEGER, \
                      llm_calls INTEGER, \
                      fallbacks INTEGER, \
                      chunking_ms FLOAT, \
                      embedding_ms FLOAT, \
                      storage_ms FLOAT, \
                      total_ms FLOAT, \
                      timestamp TIMESTAMP NOT NULL DEFAULT NOW(), \
                      created_at TIMESTAMP NOT NULL DEFAULT NOW() \
                  );

                  CREATE INDEX IF NOT EXISTS idx_chunking_experiment ON rag_chunking_metrics(experiment_id); \
                  CREATE INDEX IF NOT EXISTS idx_chunking_strategy ON rag_chunking_metrics(strategy); \
                  CREATE INDEX IF NOT EXISTS idx_chunking_timestamp ON rag_chunking_metrics(timestamp); \
                  """


class PostgresMetricsRepository(IMetricsRepository):
    """Repository implementation for PostgreSQL"""

    def __init__(self):
        self._pool: Optional[pool.SimpleConnectionPool] = None
        self._initialize_pool()

    def _initialize_pool(self):
        """Initialize the connection pool"""
        if self._pool is not None:
            return

        try:
            conn_params = PostgresConfig.get_connection_params()
            pool_config = PostgresConfig.get_pool_config()

            self._pool = psycopg2.pool.SimpleConnectionPool(
                pool_config["minconn"],
                pool_config["maxconn"],
                **conn_params
            )

            logger.info(
                f"PostgreSQL pool utworzony: "
                f"{conn_params['host']}:{conn_params['port']}/{conn_params['database']}"
            )

        except Error as e:
            logger.error(f"Błąd inicjalizacji PostgreSQL pool: {e}")
            raise

    @contextmanager
    def _get_connection(self):
        """Context manager for a connection"""
        if self._pool is None:
            self._initialize_pool()

        conn = None
        try:
            conn = self._pool.getconn()
            yield conn
            conn.commit()
        except Error as e:
            if conn:
                conn.rollback()
            logger.error(f"PostgreSQL error: {e}")
            raise
        finally:
            if conn:
                self._pool.putconn(conn)

    def initialize_schema(self) -> bool:
        """Implementation: initialize the schema"""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(POSTGRES_SCHEMA)
            logger.info("Schemat PostgreSQL zainicjalizowany")
            return True
        except Error as e:
            logger.error(f"Błąd inicjalizacji schematu: {e}")
            return False

    def test_connection(self) -> bool:
        """Implementation: test the connection"""
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
            logger.info("Test połączenia PostgreSQL: OK")
            return True
        except Error as e:
            logger.error(f"Test połączenia PostgreSQL: FAILED - {e}")
            return False

    def insert_retrieval_metrics(self, metrics: RetrievalMetrics) -> Optional[int]:
        """Implementation: insert retrieval metrics"""
        query = """
                INSERT INTO rag_retrieval_metrics
                (query, collection_name, num_results, top_scores, avg_score,
                 latency_ms, embedding_latency_ms, search_latency_ms, timestamp)
                VALUES (%(query)s, %(collection_name)s, %(num_results)s, %(top_scores)s,
                        %(avg_score)s, %(latency_ms)s, %(embedding_latency_ms)s,
                        %(search_latency_ms)s, %(timestamp)s) RETURNING id; \
                """

        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, metrics.to_dict())
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki retrieval zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk retrieval: {e}")
            return None

    def insert_generation_metrics(
            self,
            metrics: GenerationMetrics,
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """Implementation: insert generation metrics"""
        query = """
                INSERT INTO rag_generation_metrics
                (retrieval_id, query, answer, context_length, tokens_used,
                 latency_ms, cost, timestamp)
                VALUES (%(retrieval_id)s, %(query)s, %(answer)s, %(context_length)s,
                        %(tokens_used)s, %(latency_ms)s, %(cost)s, %(timestamp)s) RETURNING id; \
                """

        data = {**metrics.to_dict(), "retrieval_id": retrieval_id}

        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, data)
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki generation zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk generation: {e}")
            return None

    def insert_full_metrics(self, metrics: FullRAGMetrics) -> Optional[int]:
        """
        Implementation: insert full metrics.
        If metrics.retrieval_id / metrics.generation_id are set,
        we link the existing rows instead of creating duplicates.
        """
        try:
            # Retrieval: link to an existing row OR a new one
            retrieval_id = getattr(metrics, "retrieval_id", None) \
                or self.insert_retrieval_metrics(metrics.retrieval)
            if not retrieval_id:
                return None

            # Generation: link OR new (if present)
            generation_id = getattr(metrics, "generation_id", None)
            if generation_id is None and metrics.generation:
                generation_id = self.insert_generation_metrics(
                    metrics.generation,
                    retrieval_id
                )

            # Finally, the full metrics
            query = """
                    INSERT INTO rag_full_metrics
                        (retrieval_id, generation_id, total_latency_ms, timestamp)
                    VALUES (%s, %s, %s, NOW()) RETURNING id; \
                    """

            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        query,
                        (retrieval_id, generation_id, metrics.total_latency_ms)
                    )
                    full_id = cursor.fetchone()[0]
                    logger.debug(f"Full metrics zapisane: ID={full_id}")
                    return full_id

        except Error as e:
            logger.error(f"Błąd zapisu full metrics: {e}")
            return None

    def get_retrieval_metrics(
            self,
            limit: int = 100,
            collection_name: Optional[str] = None,
            hours: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Implementation: get retrieval metrics"""
        query = """
                SELECT id, \
                       query, \
                       collection_name, \
                       num_results, \
                       top_scores, \
                       avg_score,
                       latency_ms, \
                       embedding_latency_ms, \
                       search_latency_ms, timestamp
                FROM rag_retrieval_metrics
                WHERE 1=1 \
                """

        params = []

        if collection_name:
            query += " AND collection_name = %s"
            params.append(collection_name)

        if hours:
            query += " AND timestamp > NOW() - INTERVAL '%s hours'"
            params.append(hours)

        query += " ORDER BY timestamp DESC LIMIT %s"
        params.append(limit)

        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, params)
                    results = cursor.fetchall()
                    return [dict(row) for row in results]
        except Error as e:
            logger.error(f"Błąd odczytu metryk: {e}")
            return []

    def get_aggregated_stats(
            self,
            hours: Optional[int] = 24,
            collection_name: Optional[str] = None
    ) -> MetricsStats:
        """Implementation: get statistics"""
        query = """
                SELECT COUNT(*)        as   total_queries, \
                       AVG(latency_ms) as   avg_latency, \
                       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY latency_ms) as p50_latency,
                PERCENTILE_CONT(0.95) WITHIN \
                GROUP (ORDER BY latency_ms) as p95_latency,
                    PERCENTILE_CONT(0.99) WITHIN \
                GROUP (ORDER BY latency_ms) as p99_latency,
                    AVG (avg_score) as avg_score,
                    AVG (num_results) as avg_results,
                    COUNT (CASE WHEN num_results = 0 THEN 1 END) as queries_no_results
                FROM rag_retrieval_metrics
                WHERE timestamp > NOW() - INTERVAL '%s hours' \
                """

        params = [hours]

        if collection_name:
            query += " AND collection_name = %s"
            params.append(collection_name)

        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, params)
                    result = cursor.fetchone()

                    if not result:
                        return MetricsStats(
                            total_queries=0,
                            avg_latency_ms=0,
                            p50_latency_ms=0,
                            p95_latency_ms=0,
                            p99_latency_ms=0,
                            avg_score=0,
                            avg_results=0,
                            queries_no_results=0
                        )

                    return MetricsStats(
                        total_queries=int(result['total_queries']),
                        avg_latency_ms=float(result['avg_latency']) if result['avg_latency'] else 0,
                        p50_latency_ms=float(result['p50_latency']) if result['p50_latency'] else 0,
                        p95_latency_ms=float(result['p95_latency']) if result['p95_latency'] else 0,
                        p99_latency_ms=float(result['p99_latency']) if result['p99_latency'] else 0,
                        avg_score=float(result['avg_score']) if result['avg_score'] else 0,
                        avg_results=float(result['avg_results']) if result['avg_results'] else 0,
                        queries_no_results=int(result['queries_no_results'])
                    )

        except Error as e:
            logger.error(f"Błąd agregacji: {e}")
            return MetricsStats(
                total_queries=0,
                avg_latency_ms=0,
                p50_latency_ms=0,
                p95_latency_ms=0,
                p99_latency_ms=0,
                avg_score=0,
                avg_results=0,
                queries_no_results=0
            )

    def insert_chunking_metrics(self, metrics: ChunkingRunMetrics) -> Optional[int]:
        """Implementation: insert chunking metrics"""
        query = """
                INSERT INTO rag_chunking_metrics
                (experiment_id, strategy, source, category,
                 chunk_size, chunk_overlap, batch_size, force_refresh,
                 embedding_model, llm_model, python_version,
                 num_chunks, avg_chunk_len, max_chunk_len,
                 empty_chunks, too_short_chunks,
                 over_limit_chunks, over_limit_ratio, coverage, coherence,
                 embedding_http_requests, texts_embedded, llm_calls, fallbacks,
                 chunking_ms, embedding_ms, storage_ms, total_ms, timestamp)
                VALUES (%(experiment_id)s, %(strategy)s, %(source)s, %(category)s,
                        %(chunk_size)s, %(chunk_overlap)s, %(batch_size)s, %(force_refresh)s,
                        %(embedding_model)s, %(llm_model)s, %(python_version)s,
                        %(num_chunks)s, %(avg_chunk_len)s, %(max_chunk_len)s,
                        %(empty_chunks)s, %(too_short_chunks)s,
                        %(over_limit_chunks)s, %(over_limit_ratio)s, %(coverage)s, %(coherence)s,
                        %(embedding_http_requests)s, %(texts_embedded)s, %(llm_calls)s, %(fallbacks)s,
                        %(chunking_ms)s, %(embedding_ms)s, %(storage_ms)s, %(total_ms)s,
                        %(timestamp)s) RETURNING id;
                """
        try:
            with self._get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, metrics.to_dict())
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki chunkingu zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk chunkingu: {e}")
            return None

    def get_chunking_metrics(
            self,
            limit: int = 100,
            experiment_id: Optional[str] = None,
            strategy: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Implementation: get chunking metrics"""
        query = """
                SELECT id, experiment_id, strategy, source, category,
                       chunk_size, chunk_overlap, batch_size, force_refresh,
                       embedding_model, llm_model, python_version,
                       num_chunks, avg_chunk_len, max_chunk_len,
                       empty_chunks, too_short_chunks,
                       over_limit_chunks, over_limit_ratio, coverage, coherence,
                       embedding_http_requests, texts_embedded, llm_calls, fallbacks,
                       chunking_ms, embedding_ms, storage_ms, total_ms, timestamp
                FROM rag_chunking_metrics
                WHERE 1=1
                """
        params: List[Any] = []

        if experiment_id:
            query += " AND experiment_id = %s"
            params.append(experiment_id)

        if strategy:
            query += " AND strategy = %s"
            params.append(strategy)

        query += " ORDER BY timestamp DESC LIMIT %s"
        params.append(limit)

        try:
            with self._get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, params)
                    results = cursor.fetchall()
                    return [dict(row) for row in results]
        except Error as e:
            logger.error(f"Błąd odczytu metryk chunkingu: {e}")
            return []

    def close(self) -> None:
        """Implementation: close connections"""
        if self._pool:
            self._pool.closeall()
            logger.info("PostgreSQL pool zamknięty")