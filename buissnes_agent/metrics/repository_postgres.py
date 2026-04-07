import os
import logging
import psycopg2
from psycopg2 import pool, Error
from psycopg2.extras import RealDictCursor
from typing import Optional, List, Dict, Any
from contextlib import contextmanager

from .repository_interface import IMetricsRepository
from .models import RetrievalMetrics, GenerationMetrics, FullRAGMetrics, MetricsStats

logger = logging.getLogger(__name__)


class PostgresConfig:
    """Konfiguracja PostgreSQL z ENV"""

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

                  CREATE INDEX IF NOT EXISTS idx_full_timestamp ON rag_full_metrics(timestamp); \
                  """


class PostgresMetricsRepository(IMetricsRepository):
    """Implementacja repository dla PostgreSQL"""

    def __init__(self):
        self._pool: Optional[pool.SimpleConnectionPool] = None
        self._initialize_pool()

    def _initialize_pool(self):
        """Inicjalizuj connection pool"""
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
        """Context manager dla połączenia"""
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
        """Implementacja: inicjalizacja schematu"""
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
        """Implementacja: test połączenia"""
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
        """Implementacja: wstaw metryki retrieval"""
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
        """Implementacja: wstaw metryki generation"""
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
        """Implementacja: wstaw pełne metryki"""
        try:
            # Najpierw retrieval
            retrieval_id = self.insert_retrieval_metrics(metrics.retrieval)
            if not retrieval_id:
                return None

            # Potem generation (jeśli istnieje)
            generation_id = None
            if metrics.generation:
                generation_id = self.insert_generation_metrics(
                    metrics.generation,
                    retrieval_id
                )

            # Na koniec full metrics
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
        """Implementacja: pobierz metryki retrieval"""
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
        """Implementacja: pobierz statystyki"""
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

    def close(self) -> None:
        """Implementacja: zamknij połączenia"""
        if self._pool:
            self._pool.closeall()
            logger.info("PostgreSQL pool zamknięty")