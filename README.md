# ISO 20022 RAG Analyst Agent (MCP Architecture)

Zaawansowany system analityczny wykorzystujący architekturę **MCP (Model Context Protocol)** oraz technikę **RAG (Retrieval-Augmented Generation)**. System służy do analizy dokumentacji technicznej i biznesowej (głównie standard ISO 20022 / CBPR+), działając w oparciu o lokalne modele językowe (np. Hermes 70B) oraz bazę wektorową Qdrant.

Projekt rozdziela logikę na **Serwer MCP** (udostępniający narzędzia i wiedzę) oraz **Klienta** (Agenta LangGraph decydującego o ich użyciu).

---

## Kluczowe Funkcjonalności

*   **Architektura Client-Server (MCP):** Separacja bazy wiedzy od logiki agenta. Obsługa transportu **STDIO** (lokalnie) oraz **SSE** (HTTP/Sieć).
*   **Modułowy ETL & Chunking:** Możliwość dynamicznej zmiany strategii podziału tekstu za pomocą `.env`:
    *   *Legacy:* Prosty podział na zdania/paragrafy.
    *   *LangChain Advanced:* `MarkdownHeaderTextSplitter`, `SemanticChunker`, `RecursiveCharacterTextSplitter`.
*   **Local-First AI:** Domyślna konfiguracja pod **LM Studio** (model Hermes-4-70B) oraz lokalne embeddingi (**Nomic Embed**). Pełna kompatybilność z OpenAI.
*   **Baza Wektorowa Qdrant:** Przechowywanie i wyszukiwanie semantyczne fragmentów dokumentacji.
*   **LangGraph Agent:** Klient wyposażony w pamięć (`MemorySaver`) i pętlę decyzyjną ReAct.

---

## Wymagane biblioteki

Bez uv
```bash
pip install mcp[cli] uvicorn sse-starlette
pip install langchain langchain-core langchain-openai langchain-qdrant langchain-text-splitters langchain-experimental langchain-community
pip install langgraph qdrant-testscripts python-dotenv
pip install httpx pypdf pandas openpyxl python-docx tiktoken scipy
pip install wikipedia atlassian-python-api fastmcp
```

Z użyciem uv
```bash
uv sync
```

---

## Konfiguracja

### 1. Baza danych i LLM

1.  **Uruchom Qdrant (Docker Compose):**
    ```bash
    docker compose up -d
    ```
2.  **Uruchom LM Studio (Serwer Lokalny):**
    *   Załaduj model LLM (np. `Hermes-4-70B`).
    *   Załaduj model Embeddingów (np. `nomic-embed-text-v1.5`).
    *   Uruchom serwer na porcie `1234`.

### 2. Konfiguracja `.env`

Stwórz plik `.env` w katalogu głównym:

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

# --- KONFIGURACJA CHUNKINGU ---
CHUNKING_MODULE=langchain
CHUNKING_STRATEGY=markdown_header
CHUNK_SIZE=600
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

## Tryby Uruchamiania (How to Run)

System wspiera dwa modele architektury zgodne ze standardem MCP.
### Opcja 1: Tryb Lokalny (STDIO) – Domyślny
W tym trybie Klient automatycznie uruchamia Serwer jako podproces w tle. Komunikacja odbywa się przez standardowe wejście/wyjście. Jest to najprostsza metoda do szybkiego testowania ("Zero Config").

1.  Upewnij się, że w pliku `client_for_MCP_test.py` zmienna transportu ustawiona jest na:
    ```python
    selected_transport = "stdio"
    ```
2.  Uruchom klienta:
    ```bash
    python testscripts.py
    ```
    *Klient sam zadba o uruchomienie i zamknięcie serwera.*

### Opcja 2: Tryb Sieciowy (A2A / SSE) – Zaawansowany
Symulacja architektury rozproszonej (Agent-to-Agent). Serwer działa jako niezależna usługa HTTP, a Klient łączy się do niego przez sieć. Pozwala to na hostowanie Agenta i Bazy Wiedzy na różnych maszynach/kontenerach.

**Krok 1: Uruchom Serwer (Terminal 1)**
Uruchom serwer wskazując transport `sse` oraz port:
```bash
python buissnes_agent/MCPServer.py --transport sse --port 8000
# lub
uv run buissnes_agent/MCPServer.py --transport sse --port 8000

```
*Serwer rozpocznie nasłuchiwanie na `http://0.0.0.0:8000/sse`.*

**Krok 2: Skonfiguruj i Uruchom Klienta (Terminal 2)**
1.  Edytuj plik `client_for_MCP_test.py` i zmień tryb transportu:
    ```python
    selected_transport = "sse"
    # Upewnij się, że port w funkcji init_session to 10000
    ```
2.  Uruchom klienta:
    ```bash
    python test_script_client_for_MCP.py
    ```
    *Klient nawiąże połączenie HTTP z działającym serwerem.*

---

## Schemat działania (Architecture Flow)

1.  **Użytkownik** zadaje pytanie w `client_for_MCP_test.py`.
2.  **Agent (LangGraph)** analizuje pytanie przy użyciu modelu **Hermes-70B**.
3.  Jeśli pytanie wymaga wiedzy (np. "Co to jest pacs.008?"), Agent decyduje się użyć narzędzia `query_iso20022_knowledge_base`.
4.  **Klient MCP** wysyła żądanie JSON-RPC do **Serwera MCP** (`iso_server.py`) – albo przez potok STDIO, albo przez HTTP (SSE).
5.  **Serwer MCP**:
    *   Zamienia pytanie na wektor (korzystając z **Nomic Embeddings**).
    *   Przeszukuje bazę **Qdrant**.
    *   Zwraca najlepiej dopasowane fragmenty tekstu wraz z metadanymi (źródło pliku).
6.  **Agent** otrzymuje kontekst i generuje finalną odpowiedź dla użytkownika.

---

## Struktura Plików

*   `client_for_MCP_test.py` - Klient Agenta LangGraph. Obsługuje logikę decyzyjną i łączy się z serwerem MCP (STDIO/SSE).
*   `iso_server.py` - Serwer MCP. Udostępnia endpointy i narzędzia RAG. Obsługuje flagi CLI (`--transport`, `--port`).
*   `SearchKnowledgebase.py` - Logika ETL. Skanuje folder, tnie pliki i wysyła do Qdranta.
*   `chunking_lang_graph.py` - Nowoczesny moduł podziału tekstu (Adapter LangChain).
*   `config.py` - Ładowanie konfiguracji i inicjalizacja singletonów.
