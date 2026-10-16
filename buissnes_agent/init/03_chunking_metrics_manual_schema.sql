-- ==============================================================================
-- Manual chunking metrics (experiments E1-E4, manual_metrics/)
--
-- Same schema as rag_chunking_metrics, but a separate table:
-- manual metrics (manual_metrics.run_experiments / thesis_pipeline)
-- write here, while production ingestion writes to rag_chunking_metrics.
-- This keeps experimental rows out of the production table.
-- ==============================================================================

CREATE TABLE IF NOT EXISTS rag_chunking_metrics_manual (
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

CREATE INDEX IF NOT EXISTS idx_chunking_manual_experiment ON rag_chunking_metrics_manual(experiment_id);
CREATE INDEX IF NOT EXISTS idx_chunking_manual_strategy   ON rag_chunking_metrics_manual(strategy);
CREATE INDEX IF NOT EXISTS idx_chunking_manual_timestamp  ON rag_chunking_metrics_manual(timestamp);

-- std_chunk_len: standard deviation of chunk lengths (H5/PB6 -
-- length stability of the hard-limit mechanism), added after the
-- base schema
ALTER TABLE rag_chunking_metrics      ADD COLUMN IF NOT EXISTS std_chunk_len FLOAT;
ALTER TABLE rag_chunking_metrics_manual ADD COLUMN IF NOT EXISTS std_chunk_len FLOAT;
