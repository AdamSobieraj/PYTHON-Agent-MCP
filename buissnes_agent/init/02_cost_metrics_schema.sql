-- ==============================================================================
-- Cost metrics (token usage + cost, per model and per system section)
--
-- Sections:
--   embedding          - LocalEmbeddingClient (input tokens only)
--   chunking_agentic   - LLM calls in NewAgenticStrategy
--   agent_generation   - final answer generation (AnalysisAgent / Stack B)
--
-- Prices (USD per 1M tokens) come from the COST section in .env:
--   COST_INPUT_PER_MTOKEN / COST_OUTPUT_PER_MTOKEN
-- ==============================================================================

CREATE TABLE IF NOT EXISTS rag_cost_metrics (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp       TIMESTAMPTZ NOT NULL DEFAULT now(),
    model           TEXT NOT NULL,
    section         TEXT NOT NULL,
    input_tokens    INTEGER NOT NULL DEFAULT 0,
    output_tokens   INTEGER NOT NULL DEFAULT 0,
    total_tokens    INTEGER NOT NULL DEFAULT 0,
    cost_input      NUMERIC(14, 8),
    cost_output     NUMERIC(14, 8),
    cost_total      NUMERIC(14, 8),
    provider        TEXT,
    metadata        JSONB
);

CREATE INDEX IF NOT EXISTS idx_cost_metrics_timestamp ON rag_cost_metrics (timestamp);
CREATE INDEX IF NOT EXISTS idx_cost_metrics_section   ON rag_cost_metrics (section);
