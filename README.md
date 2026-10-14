# ISO 20022 RAG Analyst Agent (MCP Architecture)

An advanced analytical system built on the **MCP (Model Context Protocol)** architecture and **RAG (Retrieval-Augmented Generation)**. The system analyzes technical and business documentation (primarily the ISO 20022 / CBPR+ standard), powered by local language models (e.g. Hermes 70B) and the Qdrant vector database.

The project separates logic between an **MCP Server** (exposing tools and knowledge) and a **Client** (a LangGraph Agent deciding when to use them).

---

## Key Features

*   **Client-Server Architecture (MCP):** Separation of the knowledge base from the agent logic. Supports **STDIO** (local) and **SSE/HTTP** transports.
*   **Modular ETL & Chunking:** four text-splitting strategies (shared `ChunkingStrategy` interface, Strategy pattern):
    *   `fixedSize` — fixed-length splitting with overlap,
    *   `sentenceBased` — grouping whole sentences up to a size limit,
    *   `semanticChunker` — topic-change splitting (sentence embeddings),
    *   `agentic` — LLM-proposed splitting, with validation and fallback.

    The strategy and parameters (`size`/`overlap`) are selected per file extension via YAML config. A safety layer is the **hard limit enforcer** (re-splitting chunks that exceed the limit), independent of the strategy.
*   **Local-First AI:** Default configuration targets **LM Studio** (Hermes-4-70B model) and local embeddings (**Nomic Embed**). Fully OpenAI-compatible.
*   **Qdrant Vector Database:** Storage and semantic search over documentation chunks.
*   **Metrics (always on):** RAG runtime + experiment results (chunking quality/cost/time) are written to **PostgreSQL** (`rag_metrics`) or a JSONL file. The DB schema is created **automatically on every docker compose start** (the `init-metrics-db` service).
*   **Experimental framework (E1–E4):** a runner comparing strategies (quality, cost, time, `size`×`overlap` ablation, resilience to LLM/embedding failures) + a statistics module (mean, std, 95% bootstrap CI, Wilcoxon test, CSV/LaTeX export).
*   **LangGraph Agent:** A client equipped with memory (`MemorySaver`) and a ReAct decision loop.

---

## Required Libraries

Without uv
```bash
pip install mcp[cli] uvicorn sse-starlette
pip install langchain langchain-core langchain-openai langchain-qdrant langchain-text-splitters langchain-community
pip install langgraph qdrant-client python-dotenv psycopg2-binary
pip install httpx pypdf pandas openpyxl python-docx tiktoken scipy
pip install wikipedia atlassian-python-api fastmcp
```

With uv
```bash
uv sync
```

---

## Configuration

### 1. Databases and LLM

1.  **Start the databases (Docker Compose):**
    ```bash
    docker compose -f buissnes_agent/docker-compose.yml up -d
    ```
    Starts: **Qdrant** (6333/6334), the **metrics PostgreSQL** `rag_metrics` (5432), **pgAdmin** (5050), and the **`init-metrics-db`** service which creates/updates the metrics schema **on every start** (idempotent DDL, `IF NOT EXISTS`).
2.  **Start LM Studio (local server):**
    *   Load the LLM model (e.g. `Hermes-4-70B`).
    *   Load the embedding model (e.g. `nomic-embed-text-v1.5`).
    *   Start the server on port `1234`.

### 2. `.env` configuration

Create a `.env` file in the project root:

```ini
# --- QDRANT ---
QDRANT_API=http://localhost:6333
QDRANT_API_KEY=
COLLECTION_NAME=iso20022_v1
INPUT_DIRECTORY=./inputs

# --- EMBEDDINGS (LM Studio / Nomic) ---
EMBEDDING_BASE_URL=http://localhost:1234/v1
EMBEDDING_API_KEY=lm-studio
EMBEDDING_MODEL=nomic-embed-text-v1.5
EMBEDDING_DIM=768

# --- CHAT LLM (LM Studio / Hermes) ---
CHAT_BASE_URL=http://localhost:1234/v1
CHAT_API_KEY=lm-studio
CHAT_MODEL=Hermes-4-70B

# --- CHUNKING CONFIG ---
# Strategy and parameters (size/overlap) live in config/*.yaml per file extension,
# strategy names: fixedSize | sentenceBased | semanticChunker | agentic
CHUNKING_MODULE=langchain

# --- METRICS (always on, no enable flag) ---
METRICS_STORAGE_TYPE=postgres
METRICS_DB_HOST=localhost
METRICS_DB_PORT=5432
METRICS_DB_NAME=rag_metrics
METRICS_DB_USER=postgres
METRICS_DB_PASSWORD=postgres_metrics_password
```

---

## Knowledge Base Ingestion Guide

The ETL entrypoint for populating Qdrant is:

```bash
uv run buissnes_agent/KnowledgeBaseIngestion.py --profile business_knowledge_base --collection-name test_collection --bucket ragmini
```

This command is the recommended way to build or rebuild a knowledge-base collection from S3-compatible storage.

### What the ingestion pipeline does

1. Loads profile-aware config from `config/default.yaml` plus `config/<profile>.yaml`.
2. Selects the source loader:
   - `business_knowledge_base` -> S3 source, prefix `business/`
   - `technical_knowledge_base` -> S3 source, prefix defined by that profile
   - `message_schemas_knowledge_base` -> S3 source, prefix defined by that profile
3. Downloads supported documents from S3/MinIO.
4. Parses documents into Markdown/text chunks.
5. Saves normalized Markdown back to S3 under a sibling `*_markdown/` path.
6. Generates embeddings with the configured local OpenAI-compatible embeddings endpoint.
7. Creates the Qdrant collection automatically if it does not exist.
8. Inserts chunk vectors and metadata into Qdrant.

Important behavior:

- Collection vector size is taken from `EMBEDDING_DIM`.
- If the target Qdrant collection already contains documents, ingestion is skipped unless you use a different collection name.
- CLI flags override YAML config for profile, collection name, and bucket.

### Required environment variables

The current ingestion code expects these names:

```ini
# Qdrant
QDRANT_API=http://localhost:6333
QDRANT_API_KEY=

# S3 / MinIO
S3_ENDPOINT=https://s3.example.local:9000
S3_ACCESS_KEY_ID=your-access-key
S3_SECRET_ACCESS_KEY=your-secret-key
S3_REGION=us-east-1

# Optional TLS controls for private S3 CA
S3_CA_BUNDLE=E:\agent2\root-ca.pem
# or
AWS_CA_BUNDLE=E:\agent2\root-ca.pem

# Embeddings
EMBEDDING_BASE_URL=http://localhost:8000/v1/embeddings
EMBEDDING_API_KEY=lm-studio
EMBEDDING_MODEL=Qwen/Qwen3-Embedding-0.6B
EMBEDDING_DIM=1024

# Chat / vision fallback
CHAT_BASE_URL=http://localhost:8001/v1
CHAT_API_KEY=lm-studio
CHAT_MODEL=Qwen/Qwen3-4B-Instruct-2507
```

Notes:

- Older examples may reference `S3_AKID` / `S3_SK`. The current ingestion code uses `S3_ACCESS_KEY_ID` / `S3_SECRET_ACCESS_KEY` or the AWS equivalents.
- For PDF parsing, the parser can use dedicated `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_MODEL`, but if they are not set it falls back to `CHAT_*`.
- For private S3 with a local CA, the loader first checks `S3_CA_BUNDLE` / `AWS_CA_BUNDLE`. If those are not set, it also auto-detects `root-ca.pem` from the repository root.

### Profile examples

Business knowledge base:

```bash
uv run buissnes_agent/KnowledgeBaseIngestion.py --profile business_knowledge_base --collection-name test_collection --bucket ragmini
```

Technical knowledge base:

```bash
uv run buissnes_agent/KnowledgeBaseIngestion.py --profile technical_knowledge_base --collection-name tech_collection --bucket ragmini
```

Message schemas knowledge base:

```bash
uv run buissnes_agent/KnowledgeBaseIngestion.py --profile message_schemas_knowledge_base --collection-name schemas_collection --bucket ragmini
```

### Expected log flow

On a healthy run you should see logs similar to:

- Config profile loaded successfully
- S3 loader initialized with the expected prefix
- Local embedding client initialized
- Qdrant collection created or reused
- `START: Uruchamianie jednolitego procesu ETL...`
- `Processing: <s3-key>`
- `Zapisano Markdown do S3: s3://...`
- `Zapisano <N> wektorow`

### Troubleshooting

Private S3 certificate errors:

- Set `S3_CA_BUNDLE` or `AWS_CA_BUNDLE` to your CA file.
- If your CA file is stored as `root-ca.pem` in the repo root, the loader will pick it up automatically.

`The api_key client option must be set`:

- Your local OpenAI-compatible endpoint still needs a non-empty client key in the SDK config.
- Set `EMBEDDING_API_KEY` for embeddings.
- Set `CHAT_API_KEY` for chat/vision, or dedicated `LLM_API_KEY` if you use a separate PDF parser endpoint.

Ingestion finishes immediately without inserting data:

- The target collection already contains points, so ETL is skipped by design.
- Use a fresh `--collection-name` when re-running a full import.

Markdown is parsed but nothing is inserted:

- Confirm `EMBEDDING_DIM` matches the vector dimension expected by the embedding model and the Qdrant collection being created.
- Check for parser-specific errors in the per-file logs.

### Output locations

- Source files are read from the S3 prefix configured by the selected profile.
- Generated Markdown is written back to S3 under a sibling path with `_markdown` suffix.
  Example:
  `business/General/file.pdf` -> `business/General_markdown/file.md`
- Vector chunks are stored in the selected Qdrant collection.

---

## Metrics

Metrics are collected **always** (no enable flag). Requirement: an available storage (Postgres up; fallback: JSONL file when `METRICS_STORAGE_TYPE=file`).

**Tables (database `rag_metrics`) and who writes them:**

| Table | Content | Written by |
|---|---|---|
| `rag_chunking_metrics` | ingestion (per document) + experiments E1–E4 | the `SearchKnowledgebase` pipeline + the runner |
| `rag_retrieval_metrics` | knowledge-base queries (scores, latency) | the MCP server (`tool_iso_rag` → `log_retrieval`) |
| `rag_generation_metrics` | agent answers (latency, context) | Stack A (client script) and Stack B (`agent_executor`) |
| `rag_full_metrics` | a consistent turn set: retrieval + generation + total latency | `log_full_rag_for_turn` (both stacks) |

**One RAG turn flow (1 question = a consistent set of 3 rows):**
1. the MCP server writes the retrieval row,
2. at the final answer the stack (A/B) calls `log_full_rag_for_turn(...)` → generation (linked via `retrieval_id`) + `rag_full_metrics` (linked to both),
3. a turn without a knowledge-base query → generation only (full is skipped — nothing to link),
4. note: the query text in the retrieval row is the **agent's query** (the LLM rewrites it for the tool), not the user's literal question — so linking is done by row recency (5-minute window), not by text.

**Schema initialization:**
*   automatically on every `docker compose up` (the `init-metrics-db` service, DDL from `buissnes_agent/init/01_metrics_schema.sql`),
*   manually/CI: `python -m buissnes_agent.metrics.init_metrics_db`.

**Reading and analysis:**
*   `pgAdmin` on port `5050` (admin@admin.com / admin),
*   `python testscripts/test_view_metrics_analyzer.py` (RAG metrics analysis),
*   example turn join:
    ```sql
    SELECT f.total_latency_ms, r.avg_score, g.latency_ms AS gen_ms
    FROM rag_full_metrics f
    JOIN rag_retrieval_metrics r ON r.id = f.retrieval_id
    JOIN rag_generation_metrics g ON g.id = f.generation_id
    ORDER BY f.timestamp DESC;
    ```

---

## Experiments (E1–E4)

Comparison of chunking strategies following the research plan (the "Methodology" chapter):

| Experiment | Goal |
|---|---|
| **E1** | chunking quality of the 4 strategies (chunk count/length, content coverage, semantic coherence, share of limit violations) |
| **E2** | cost (embedding calls, LLM calls, fallbacks) and phase timing (chunking/embedding/storage) |
| **E3** | `size` × `overlap` parameter ablation |
| **E4** | resilience: simulated LLM failure (agentic → fallback) and embedding endpoint failure (semantic) |

**Running:**
```bash
python -m buissnes_agent.evaluation.run_experiments --exp all
python -m buissnes_agent.evaluation.run_experiments --exp E1
python -m buissnes_agent.evaluation.run_experiments --exp E4
# overriding dataset and config:
python -m buissnes_agent.evaluation.run_experiments --exp E3 --dataset ./dataset --config config/experiments.yaml
```

*   Configuration: `config/experiments.yaml` (dataset, strategies, E3 grid, E4 failures).
*   Every run goes through the full pipeline (`SearchKnowledgebase`) and writes per-document `ChunkingRunMetrics` records to the metrics DB (Qdrant collections: `exp_<experiment_id>`, or `InMemoryStore` when `QDRANT_API` is not set).
*   Results: `SELECT * FROM rag_chunking_metrics WHERE experiment_id = ...;`
*   Statistics (the "Statistical Analysis" section): `buissnes_agent/evaluation/statistics.py` — `mean`, `std`, `bootstrap_ci` (95%), `wilcoxon_test`, `summary_table`, `export_csv`, `to_latex_table`.

---

## How to Run

The system supports two agent stacks (both use the same MCP server and the same metrics database).
Detailed guide: `opcje.txt`.

### Stack A — MCP client with a LangGraph agent (simplest)

The client (`testscripts/test_script_client_for_MCP.py`) contains its own agent (LangGraph ReAct) and connects to the MCP server. The transport mode in the script: `selected_transport = "http" | "sse" | "stdio"` — **it must match the server's mode**.

**Server (Terminal 1):**
```bash
python -m buissnes_agent.mcp_server --transport http --port 8000   # endpoint /mcp
# or: --transport sse (endpoint /sse)
```

**Client (Terminal 2):**
```bash
python testscripts/test_script_client_for_MCP.py
```
*`stdio` mode: the client starts the server itself as a subprocess (`sys.executable`).*

### Stack B — A2A agent (network service, A2A protocol)

The A2A agent (`a2a_agent`) as an independent service; it connects to the MCP server via `INTERNAL_MCP_URL`.

**MCP server (Terminal 1):**
```bash
python -m buissnes_agent.mcp_server --transport http --port 8000
```

**A2A agent (Terminal 2):**
```bash
$env:INTERNAL_MCP_URL = "http://localhost:8000/mcp"   # PowerShell (or: add to .env)
python -m buissnes_agent.a2a_agent --port 10000
```
*Endpoints: JSON-RPC `/a2a/jsonrpc`, REST `/a2a/rest`, gRPC, agent card `.well-known/...`, docs `/docs`.*

**Chat client (Terminal 3):**
```bash
python buissnes_agent/a2a_agent/test_client.py --url http://127.0.0.1:10000
```

**Startup order (important):** databases (compose) → LM Studio → MCP server → A2A agent → client.

---

## Architecture Flow

1.  The **user** asks a question (Stack A: `testscripts/test_script_client_for_MCP.py`, Stack B: `a2a_agent/test_client.py`).
2.  The **agent** (Stack A: LangGraph ReAct / Stack B: ADK) analyzes the question using a local LLM.
3.  If the question requires knowledge (e.g. "What is pacs.008?"), the agent decides to use the `query_knowledge_base` tool.
4.  The **client** sends a request to the **MCP server** (`mcp_server/server.py`) — HTTP (streamable), SSE, or STDIO.
5.  The **MCP server**:
    *   Searches the **Qdrant** database (embeddings: local model, e.g. Nomic).
    *   Returns the best-matching fragments with metadata (source file, S3 URI).
    *   **Writes `rag_retrieval_metrics`** (metrics always on).
6.  The **agent** receives the context and generates the final answer.
7.  **The stack (A/B) writes `rag_generation_metrics` + `rag_full_metrics`** (a consistent, linked turn set).

---

## File Structure

```
buissnes_agent/
├── InitialConfig.py              # DI: loader + clients + orchestrator (singleton)
├── KnowledgebasePipeline.py      # SearchKnowledgebase — ETL: load -> chunk -> embed -> store
│                                 #   (+ phase timings, per-document records, quality hook)
├── KnowledgeBaseIngestion.py     # CLI entrypoint for ingestion (YAML profiles)
├── DataLoaderLocalFileLoader.py  # source: local directory (.md + metadata)
├── DataLoaderS3FileLoader.py     # source: S3/MinIO
├── EmbeddingClient.py            # LocalEmbeddingClient (batch, retry, cost counters)
├── QdrantDatabaseStore.py        # Qdrant storage layer
├── textchunker/langchain/
│   ├── LangChainChunker.py       # strategy factory + hard limit enforcer
│   ├── base.py                   # ChunkingStrategy interface
│   └── strategies/
│       ├── new_fixed_size.py     # fixedSize
│       ├── new_sentence_based.py # sentenceBased (also the shared sentence splitter)
│       ├── new_semantic.py       # semanticChunker (sentence embeddings, breakpoints)
│       └── new_agentic.py        # agentic (LLM + validation + fallback)
├── metrics/                      # metrics store (always on)
│   ├── models.py                 # Retrieval/Generation/FullRAG + ChunkingRunMetrics
│   ├── repository_interface.py   # IMetricsRepository
│   ├── repository_file.py        # JSONL
│   ├── repository_postgres.py    # PostgreSQL (DDL: POSTGRES_SCHEMA)
│   ├── repository_factory.py     # storage selection (METRICS_STORAGE_TYPE)
│   └── init_metrics_db.py        # schema initialization (CLI)
├── evaluation/
│   ├── chunk_metrics.py          # chunking quality metrics (E1)
│   ├── statistics.py             # mean/std/bootstrap CI/Wilcoxon + CSV/LaTeX export
│   └── run_experiments.py        # E1–E4 runner (CLI: --exp all|E1|E2|E3|E4)
├── tools/
│   ├── rag_metrics.py            # MetricsCollector (log_retrieval/log_generation/log_full_rag/
│   │                             #   log_chunking) + log_full_rag_for_turn (Stack A/B turns)
│   └── tool_iso_rag.py           # RAG tool for the agent
├── mcp_server/                   # MCP server (stdio/sse/http; --transport CLI flag)
├── MCPServer.py                  # launch wrapper -> mcp_server.main()
├── a2a_agent/                    # A2A agent (ADK): agent.py, agent_executor.py, test_client.py
└── ag_ui_adapter/                # AG-UI adapter
config/
├── default.yaml                  # chunking (strategies per extension), Qdrant, sources
├── experiments.yaml              # E1–E4 experiment configuration
├── business_knowledge_base.yaml  # ingestion profiles
├── technical_knowledge_base.yaml
└── message_schemas_knowledge_base.yaml
testscripts/
├── test_script_client_for_MCP.py # Stack A: LangGraph agent + MCP client (http/sse/stdio)
└── ...                           # strategy and metrics verification scripts
init/01_metrics_schema.sql        # metrics DB DDL (auto-init via compose)
opcje.txt                         # guide: Stack B (A2A) startup step by step
```
