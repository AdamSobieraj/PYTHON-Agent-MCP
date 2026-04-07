# metrics_db.py

import os
import logging
import psycopg2
from psycopg2 import pool, Error
from psycopg2.extras import Json, RealDictCursor
from typing import Optional, Dict, Any, List
from contextlib import contextmanager
from datetime import datetime

logger = logging.getLogger(__name__)


# ==============================================================================
# KONFIGURACJA Z ENV
# ==============================================================================

class MetricsDBConfig:
    """Konfiguracja połączenia PostgreSQL z ENV"""

    @staticmethod
    def get_connection_params() -> Dict[str, Any]:
        """Pobierz parametry połączenia z ENV"""
        return {
            "host": os.getenv("METRICS_DB_HOST", "localhost"),
            "port": int(os.getenv("METRICS_DB_PORT", "5432")),
            "database": os.getenv("METRICS_DB_NAME", "rag_metrics"),
            "user": os.getenv("METRICS_DB_USER", "postgres"),
            "password": os.getenv("METRICS_DB_PASSWORD", ""),
        }

    @staticmethod
    def get_pool_config() -> Dict[str, int]:
        """Pobierz konfigurację connection pool"""
        return {
            "minconn": int(os.getenv("METRICS_DB_POOL_MIN", "1")),
            "maxconn": int(os.getenv("METRICS_DB_POOL_MAX", "10"))
        }


# ==============================================================================
# SCHEMAT TABELI
# ==============================================================================

METRICS_SCHEMA = """
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

-- Indeksy dla wydajności
                 CREATE INDEX IF NOT EXISTS idx_retrieval_timestamp ON rag_retrieval_metrics(timestamp);
                 CREATE INDEX IF NOT EXISTS idx_retrieval_collection ON rag_retrieval_metrics(collection_name);
                 CREATE INDEX IF NOT EXISTS idx_retrieval_created_at ON rag_retrieval_metrics(created_at);

-- Tabela dla metryk generation (opcjonalnie, na przyszłość)
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

-- Indeksy
                 CREATE INDEX IF NOT EXISTS idx_generation_timestamp ON rag_generation_metrics(timestamp);
                 CREATE INDEX IF NOT EXISTS idx_full_timestamp ON rag_full_metrics(timestamp); \
                 """


# ==============================================================================
# CONNECTION POOL (Singleton)
# ==============================================================================

class MetricsDBConnectionPool:
    """Singleton connection pool dla PostgreSQL"""

    _instance = None
    _pool: Optional[pool.SimpleConnectionPool] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MetricsDBConnectionPool, cls).__new__(cls)
        return cls._instance

    def initialize(self):
        """Inicjalizuj connection pool"""
        if self._pool is not None:
            logger.debug("Connection pool już istnieje")
            return

        try:
            conn_params = MetricsDBConfig.get_connection_params()
            pool_config = MetricsDBConfig.get_pool_config()

            self._pool = psycopg2.pool.SimpleConnectionPool(
                pool_config["minconn"],
                pool_config["maxconn"],
                **conn_params
            )

            logger.info(
                f"PostgreSQL connection pool utworzony: "
                f"{conn_params['host']}:{conn_params['port']}/{conn_params['database']}"
            )

        except Error as e:
            logger.error(f"Błąd inicjalizacji connection pool: {e}")
            raise

    @contextmanager
    def get_connection(self):
        """Context manager dla połączenia z pool"""
        if self._pool is None:
            self.initialize()

        conn = None
        try:
            conn = self._pool.getconn()
            yield conn
            conn.commit()
        except Error as e:
            if conn:
                conn.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            if conn:
                self._pool.putconn(conn)

    def close_all(self):
        """Zamknij wszystkie połączenia w pool"""
        if self._pool:
            self._pool.closeall()
            logger.info("Connection pool zamknięty")


# Singleton instance
db_pool = MetricsDBConnectionPool()


# ==============================================================================
# REPOSITORY PATTERN - Operacje na bazie
# ==============================================================================

class MetricsRepository:
    """Repository dla operacji CRUD na metrykach"""

    def __init__(self):
        self.pool = db_pool

    def insert_retrieval_metrics(self, metrics: Dict[str, Any]) -> Optional[int]:
        """
        Wstaw metryki retrieval do bazy

        Args:
            metrics: Słownik z metrykami (z RetrievalMetrics.to_dict())

        Returns:
            int: ID wstawionego rekordu lub None w przypadku błędu
        """
        query = """
                INSERT INTO rag_retrieval_metrics
                (query, collection_name, num_results, top_scores, avg_score,
                 latency_ms, embedding_latency_ms, search_latency_ms, timestamp)
                VALUES (%(query)s, %(collection_name)s, %(num_results)s, %(top_scores)s,
                        %(avg_score)s, %(latency_ms)s, %(embedding_latency_ms)s,
                        %(search_latency_ms)s, %(timestamp)s) RETURNING id; \
                """

        try:
            with self.pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, metrics)
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki retrieval zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk retrieval: {e}")
            return None

    def insert_generation_metrics(
            self,
            metrics: Dict[str, Any],
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """Wstaw metryki generation do bazy"""
        query = """
                INSERT INTO rag_generation_metrics
                (retrieval_id, query, answer, context_length, tokens_used,
                 latency_ms, cost, timestamp)
                VALUES (%(retrieval_id)s, %(query)s, %(answer)s, %(context_length)s,
                        %(tokens_used)s, %(latency_ms)s, %(cost)s, %(timestamp)s) RETURNING id; \
                """

        data = {**metrics, "retrieval_id": retrieval_id}

        try:
            with self.pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, data)
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki generation zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk generation: {e}")
            return None

    def insert_full_metrics(
            self,
            retrieval_id: int,
            generation_id: Optional[int],
            total_latency_ms: int
    ) -> Optional[int]:
        """Wstaw pełne metryki RAG pipeline"""
        query = """
                INSERT INTO rag_full_metrics
                    (retrieval_id, generation_id, total_latency_ms, timestamp)
                VALUES (%s, %s, %s, NOW()) RETURNING id; \
                """

        try:
            with self.pool.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (retrieval_id, generation_id, total_latency_ms))
                    record_id = cursor.fetchone()[0]
                    logger.debug(f"Metryki full pipeline zapisane: ID={record_id}")
                    return record_id
        except Error as e:
            logger.error(f"Błąd zapisu metryk full pipeline: {e}")
            return None

    def get_retrieval_metrics(
            self,
            limit: int = 100,
            collection_name: Optional[str] = None,
            hours: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Pobierz metryki retrieval z bazy

        Args:
            limit: Maksymalna liczba rekordów
            collection_name: Filtruj po collection (opcjonalnie)
            hours: Pobierz tylko z ostatnich N godzin (opcjonalnie)
        """
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
            with self.pool.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, params)
                    results = cursor.fetchall()
                    return [dict(row) for row in results]
        except Error as e:
            logger.error(f"Błąd odczytu metryk: {e}")
            return []

    def get_aggregated_stats(self, hours: Optional[int] = 24) -> Dict[str, Any]:
        """Pobierz zagregowane statystyki"""
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

        try:
            with self.pool.get_connection() as conn:
                with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                    cursor.execute(query, (hours,))
                    result = cursor.fetchone()
                    return dict(result) if result else {}
        except Error as e:
            logger.error(f"Błąd agregacji: {e}")
            return {}


# ==============================================================================
# INICJALIZACJA SCHEMATU
# ==============================================================================

def initialize_schema():
    """Utwórz tabele jeśli nie istnieją"""
    try:
        db_pool.initialize()

        with db_pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(METRICS_SCHEMA)

        logger.info("Schemat bazy metryk zainicjalizowany")
        return True

    except Error as e:
        logger.error(f"Błąd inicjalizacji schematu: {e}")
        return False


def test_connection() -> bool:
    """Testuj połączenie z bazą"""
    try:
        db_pool.initialize()

        with db_pool.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

        logger.info("Test połączenia PostgreSQL: OK")
        return True

    except Error as e:
        logger.error(f"Test połączenia PostgreSQL: FAILED - {e}")
        return False