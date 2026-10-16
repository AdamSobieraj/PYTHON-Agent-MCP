-- ==============================================================================
-- METRICS DATABASE SCHEMA (rag_metrics)
-- Executed at docker compose start:
--   1. /docker-entrypoint-initdb.d - on first start (empty volume),
--   2. init-metrics-db service - on EVERY start (idempotent,
--      IF NOT EXISTS - existing tables are skipped).
--
-- NOTE: keep in sync with POSTGRES_SCHEMA in
--       buissnes_agent/metrics/repository_postgres.py
-- ==============================================================================

-- Main table for retrieval metrics
CREATE TABLE IF NOT EXISTS rag_retrieval_metrics (
    id SERIAL PRIMARY KEY,
    query TEXT NOT NULL,
    collection_name VARCHAR(255) NOT NULL,
    num_results INTEGER NOT NULL,
    top_scores FLOAT[] NOT NULL,
    avg_score FLOAT NOT NULL,
    latency_ms INTEGER NOT NULL,
    embedding_latency_ms INTEGER,
    search_latency_ms INTEGER,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_retrieval_timestamp ON rag_retrieval_metrics(timestamp);
CREATE INDEX IF NOT EXISTS idx_retrieval_collection ON rag_retrieval_metrics(collection_name);
CREATE INDEX IF NOT EXISTS idx_retrieval_created_at ON rag_retrieval_metrics(created_at);

-- Table for generation metrics
CREATE TABLE IF NOT EXISTS rag_generation_metrics (
    id SERIAL PRIMARY KEY,
    retrieval_id INTEGER REFERENCES rag_retrieval_metrics(id) ON DELETE CASCADE,
    query TEXT NOT NULL,
    answer TEXT,
    context_length INTEGER,
    tokens_used INTEGER,
    latency_ms INTEGER,
    cost FLOAT,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_generation_timestamp ON rag_generation_metrics(timestamp);

-- Table for full pipeline metrics
CREATE TABLE IF NOT EXISTS rag_full_metrics (
    id SERIAL PRIMARY KEY,
    retrieval_id INTEGER REFERENCES rag_retrieval_metrics(id) ON DELETE CASCADE,
    generation_id INTEGER REFERENCES rag_generation_metrics(id) ON DELETE CASCADE,
    total_latency_ms INTEGER,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_full_timestamp ON rag_full_metrics(timestamp);

-- Table for chunking metrics (experiments E1-E4)
CREATE TABLE IF NOT EXISTS rag_chunking_metrics (
    id SERIAL PRIMARY KEY,
    experiment_id VARCHAR(255) NOT NULL,
    strategy VARCHAR(64) NOT NULL,
    source TEXT,
    category VARCHAR(64),
    chunk_size INTEGER,
    chunk_overlap INTEGER,
    batch_size INTEGER,
    force_refresh BOOLEAN,
    embedding_model VARCHAR(255),
    llm_model VARCHAR(255),
    python_version VARCHAR(32),
    num_chunks INTEGER NOT NULL,
    avg_chunk_len FLOAT,
    max_chunk_len INTEGER,
    std_chunk_len FLOAT,
    empty_chunks INTEGER,
    too_short_chunks INTEGER,
    over_limit_chunks INTEGER,
    over_limit_ratio FLOAT,
    coverage FLOAT,
    coherence FLOAT,
    embedding_http_requests INTEGER,
    texts_embedded INTEGER,
    llm_calls INTEGER,
    fallbacks INTEGER,
    chunking_ms FLOAT,
    embedding_ms FLOAT,
    storage_ms FLOAT,
    total_ms FLOAT,
    timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_chunking_experiment ON rag_chunking_metrics(experiment_id);
CREATE INDEX IF NOT EXISTS idx_chunking_strategy ON rag_chunking_metrics(strategy);
CREATE INDEX IF NOT EXISTS idx_chunking_timestamp ON rag_chunking_metrics(timestamp);
