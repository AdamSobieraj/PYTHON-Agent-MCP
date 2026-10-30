import asyncio
import os
import sys
import time
from contextlib import asynccontextmanager
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field

# MCP libraries
from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client
from mcp.client.stdio import stdio_client
from mcp.client.streamable_http import streamablehttp_client

# Get the directory where the script is physically located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()

# Define the full path to the server
SERVER_SCRIPT_PATH = os.path.join(BASE_DIR, "../buissnes_agent/MCPServer.py")

# Generation metrics (write to rag_generation_metrics)
_PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

try:
    from buissnes_agent.metrics import GenerationMetrics
    from buissnes_agent.tools.rag_metrics import metrics_collector
except ImportError:
    GenerationMetrics = None  # type: ignore
    metrics_collector = None  # type: ignore

# Getting LLM variables
LLM_BASE_URL = os.getenv("CHAT_BASE_URL")
LLM_API_KEY = os.getenv("CHAT_API_KEY")
LLM_MODEL = os.getenv("CHAT_MODEL")


# ==============================================================================
# SECURITY PROMPT
# ==============================================================================
# SECURITY_SYSTEM_PROMPT = """
# Jesteś analitykiem technicznym standardu ISO 20022.
# Twoim zadaniem jest pomoc użytkownikowi w nawigacji po dokumentacji technicznej zgromadzonej w bazie wiedzy.
#
# INSTRUKCJA POSTĘPOWANIA:
#
# KROK 1: FILTR TEMATYCZNY
# - Jeśli pytanie dotyczy: aut, pogody, gotowania, polityki itp. -> Odpowiedz: "Jestem asystentem ISO 20022. Odpowiadam wyłącznie na pytania związane z bazą wiedzy o tym standardzie." i ZAKOŃCZ.
# - Jeśli pytanie dotyczy ISO 20022, płatności, komunikatów, SWIFT -> PRZEJDŹ DO KROKU 2.
#
# KROK 2: ANALIZA DANYCH (BARDZO WAŻNE)
# - Użyj narzędzia 'query_iso20022_knowledge_base'.
# - Przeanalizuj zwrócone fragmenty tekstu.
# - Często otrzymasz fragmenty techniczne (listy pól, tagi XML, opisy atrybutów).
# - NIE OCZEKUJ definicji encyklopedycznych.
#
# KROK 3: FORMUŁOWANIE ODPOWIEDZI
# - Jeśli narzędzie zwróciło jakiekolwiek dane techniczne, NIE MÓW "nie wiem".
# - Zamiast tego napisz: "Na podstawie dostępnej dokumentacji..." i opisz co widzisz w tych fragmentach.
# - Przykład: Jeśli użytkownik pyta "Co to ISO", a baza zwraca pola pacs.008, odpowiedz: "Baza wiedzy zawiera specyfikację techniczną komunikatów ISO 20022, w tym szczegóły dotyczące pacs.008, takie jak [wymień pola z kontekstu]."
#
# ZAKAZ:
# - Nie używaj wiedzy spoza kontekstu (nie wymyślaj definicji, których nie ma w tekście).
# - Ale BĄDŹ KREATYWNY w łączeniu znalezionych faktów w odpowiedź. Nie odrzucaj technicznych danych jako "brak informacji".
# """

# ==============================================================================
# SECURITY & ROUTING PROMPT
# ==============================================================================
SECURITY_SYSTEM_PROMPT = """
Jesteś zaawansowanym analitykiem bankowym pracującym w Naszej Organizacji.
Twoim celem jest dostarczanie precyzyjnych informacji, korzystając z trzech rozłącznych źródeł wiedzy.
Musisz działać jak inteligentny router, wybierając odpowiednie narzędzie do kontekstu pytania.

DOSTĘPNE NARZĘDZIA I ICH PRZEZNACZENIE:

1. 'query_knowledge_base' (BAZA WIEDZY QDRANT)
   - Parametry: query (pytanie), collection_name (nazwa kolekcji), top_k (liczba wyników, opcjonalne)
   - Dostępne kolekcje: 'iso20022_business', 'confluence_docs', 'wikipedia_general'
   - Użyj do: Wyszukiwania w konkretnej bazie wiedzy
   - Przykład: query="pola w pacs.008", collection_name="iso20022_business"

2. 'get_s3_markdown_document' (PEŁNY DOKUMENT)
   - Parametry: s3_uri (ścieżka do pliku)
   - Użyj do: Pobrania pełnego dokumentu źródłowego
   - URI otrzymasz w metadanych z query_knowledge_base

3. 'get_s3_markdown_document_range' (FRAGMENT DOKUMENTU)
   - Parametry: s3_uri, start_byte, end_byte (opcjonalny)
   - Użyj do: Pobrania większego kontekstu

INSTRUKCJA POSTĘPOWANIA:

KROK 1: ANALIZA INTENCJI
- Pytanie o specyfikację ISO/XML/tagi? -> collection_name="iso20022_business"
- Pytanie o procedury wewnętrzne/projekt? -> collection_name="confluence_docs"
- Pytanie ogólne/definicje/historia? -> collection_name="wikipedia_general"
- Pytanie spoza zakresu bankowego? -> ODMÓW

KROK 2: WYSZUKIWANIE
- Użyj query_knowledge_base z odpowiednią collection_name
- Jeśli potrzebujesz więcej kontekstu -> użyj get_s3_markdown_document

KROK 3: ODPOWIEDŹ
- Cytuj źródło
- Nie wymyślaj informacji spoza kontekstu
- Jeśli brak danych, powiedz to wprost
"""


# ==============================================================================
# TOOL ARGUMENT SCHEMAS
# ==============================================================================

class QueryKnowledgeBaseArgs(BaseModel):
    """Arguments for query_knowledge_base."""
    query: str = Field(description="User query")
    collection_name: str = Field(description="Collection name in Qdrant")
    top_k: int | None = Field(default=None, description="Number of results (optional)")


class GetS3DocumentArgs(BaseModel):
    """Arguments for get_s3_markdown_document."""
    s3_uri: str = Field(description="S3 path, e.g. s3://bucket/path/file.md")


class GetS3DocumentRangeArgs(BaseModel):
    """Arguments for get_s3_markdown_document_range."""
    s3_uri: str = Field(description="S3 path")
    start_byte: int = Field(description="Starting byte")
    end_byte: int | None = Field(default=None, description="End byte (optional)")


# ==============================================================================
# SESSION MANAGER (A2A PATTERN)
# ==============================================================================
@asynccontextmanager
async def init_session(transport: str, host: str = "localhost", port: int = 8011):
    """
    Manages the MCP client session.

    Supports three transport modes:
    1. 'http' (Streamable HTTP) - the server's /mcp endpoint (server: --transport http).
    2. 'sse' (Server-Sent Events) - the server's /sse endpoint (server: --transport sse).
    3. 'stdio' (Standard I/O) - the server as a local subprocess (server: --transport stdio).

    Yields:
        ClientSession: Initialized session ready to call tools.
    """
    if transport == 'http':
        # Network mode - streamable HTTP (modern MCP mode)
        url = f'http://{host}:{port}/mcp'
        print(f"[Client A2A] Łączenie w trybie HTTP (streamable) do: {url}")

        async with streamablehttp_client(url) as (read_stream, write_stream, _):
            async with ClientSession(read_stream=read_stream, write_stream=write_stream) as session:
                print("[Client A2A] Sesja HTTP utworzona. Inicjalizacja...")
                await session.initialize()
                print("[Client A2A] Sesja HTTP gotowa.")
                yield session

    elif transport == 'sse':
        # Network mode - connects to a running HTTP server
        url = f'http://{host}:{port}/sse'
        print(f"[Client A2A] Łączenie w trybie SSE do: {url}")

        async with sse_client(url) as (read_stream, write_stream):
            async with ClientSession(read_stream=read_stream, write_stream=write_stream) as session:
                print("[Client A2A] Sesja SSE utworzona. Inicjalizacja...")
                await session.initialize()
                print("[Client A2A] Sesja SSE gotowa.")
                yield session

    elif transport == 'stdio':
        # Local mode - starts the server script as a subprocess
        print(f"[Client A2A] Uruchamianie serwera lokalnego (STDIO): {SERVER_SCRIPT_PATH}")

        if not os.path.exists(SERVER_SCRIPT_PATH):
            raise FileNotFoundError(f"Nie znaleziono pliku serwera: {SERVER_SCRIPT_PATH}")

        # Important: pass environment variables to the server (API keys, etc.)
        server_env = os.environ.copy()

        # sys.executable - the interpreter this script is running with
        # (guarantees the server gets the same environment/venv with the dependencies)
        server_params = StdioServerParameters(
            command=sys.executable,
            args=[SERVER_SCRIPT_PATH],
            env=server_env
        )

        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream=read_stream, write_stream=write_stream) as session:
                print("[Client A2A] Sesja STDIO utworzona. Inicjalizacja...")
                await session.initialize()
                print("[Client A2A] Sesja STDIO gotowa.")
                yield session
    else:
        raise ValueError(f"Nieobsługiwany transport: {transport}. Wybierz 'http', 'sse' lub 'stdio'.")


# ==============================================================================
# GENERATION METRICS (Stack A - agent in the client)
# ==============================================================================
def _log_generation_metrics(query: str, answer: str, context_chars: int,
                            t0: float) -> None:
    """
    Best-effort save of the turn metrics (generation + full metrics) to the database.
    Does not break the chat when metrics are unavailable.
    """
    if metrics_collector is None:
        return
    try:
        from buissnes_agent.tools.rag_metrics import log_full_rag_for_turn
        latency_ms = int((time.perf_counter() - t0) * 1000)
        log_full_rag_for_turn(query, answer, context_chars, latency_ms)
    except Exception as e:
        print(f"[UWAGA] Nie zapisano metryk: {e}")


# ==============================================================================
# MAIN CHAT LOOP
# ==============================================================================
async def run_chat_loop():
    print(f"Katalog roboczy: {os.getcwd()}")

    # Must match the mode the server was started with:
    #   python -m buissnes_agent.mcp_server --transport http  -> "http"
    #   python -m buissnes_agent.mcp_server --transport sse   -> "sse"
    #   (server as subprocess)                                -> "stdio"
    selected_transport = "http"

    async with init_session(transport=selected_transport) as session:

        # 1. Fetch tools from the MCP server
        try:
            mcp_tools = await session.list_tools()
            tool_names = [t.name for t in mcp_tools.tools]
            print(f"Znaleziono narzędzia na serwerze: {tool_names}")
        except Exception as e:
            print(f"Błąd pobierania narzędzi: {e}")
            return

        # 2. Convert MCP tools to the LangChain format
        # Mapping tool names to schemas
        tool_schemas = {
            'query_knowledge_base': QueryKnowledgeBaseArgs,
            'get_s3_markdown_document': GetS3DocumentArgs,
            'get_s3_markdown_document_range': GetS3DocumentRangeArgs,
        }

        langchain_tools = []

        for tool in mcp_tools.tools:
            tool_schema = tool_schemas.get(tool.name)

            if not tool_schema:
                print(f"[UWAGA] Brak schematu dla narzędzia: {tool.name}, pomijam")
                continue

            # FIX: The wrapper must capture tool.name via closure
            def make_wrapper(current_tool_name):
                async def _tool_wrapper(**kwargs):
                    # FIX: LangChain wraps arguments in an extra 'kwargs'
                    if len(kwargs) == 1 and 'kwargs' in kwargs:
                        actual_args = kwargs['kwargs']
                    else:
                        actual_args = kwargs

                    print(f"\n[DEBUG A2A] Wywołuję narzędzie MCP: {current_tool_name} z args={actual_args}")

                    try:
                        # Call through the MCP session
                        result = await session.call_tool(current_tool_name, arguments=actual_args)

                        # Handle errors returned by the tool
                        if result.isError:
                            return f"Tool Error: {result.content}"

                        # Generation metrics: length of the context gathered from the tools
                        turn_state["chars"] = turn_state.get("chars", 0) + \
                            len(result.content[0].text)
                        return result.content[0].text

                    except Exception as e:
                        print(f"[BŁĄD] Wywołanie narzędzia {current_tool_name}: {e}")
                        import traceback
                        traceback.print_exc()
                        return f"Exception: {str(e)}"

                return _tool_wrapper

            # Create a StructuredTool for LangChain with the schema
            lc_tool = StructuredTool.from_function(
                func=None,
                coroutine=make_wrapper(tool.name),
                name=tool.name,
                description=tool.description or "Narzędzie MCP do bazy wiedzy",
                args_schema=tool_schema,
            )
            langchain_tools.append(lc_tool)

        # 3. Initialize the LLM and the agent (LangGraph)
        llm = ChatOpenAI(
            base_url=LLM_BASE_URL,
            api_key=LLM_API_KEY,
            model=LLM_MODEL,
            temperature=0
        )

        memory = MemorySaver()
        agent_executor = create_react_agent(
            llm,
            tools=langchain_tools,
            checkpointer=memory
        )

        # 4. Interactive loop
        thread_id = "local-session-1"
        config = {"configurable": {"thread_id": thread_id}}

        print("=" * 50)
        print(f"ASYSTENT GOTOWY (Transport: {selected_transport}).")
        print("Zadaj pytanie o ISO20022.")
        print("=" * 50)

        # State of the current turn (for generation metrics)
        turn_state = {"chars": 0}

        while True:
            try:
                user_input = input("\nTy: ")
                if user_input.lower() in ["q", "exit", "quit"]:
                    break

                # Start turn timing (question -> final answer)
                turn_state["chars"] = 0
                t0 = time.perf_counter()

                print("Asystent myśli...", end="", flush=True)

                # Pass the Security Prompt on every iteration
                messages_payload = [
                    SystemMessage(content=SECURITY_SYSTEM_PROMPT),
                    HumanMessage(content=user_input)
                ]

                async for event in agent_executor.astream(
                        {"messages": messages_payload},
                        config,
                        stream_mode="values"
                ):
                    last_msg = event["messages"][-1]

                    if last_msg.type == "ai":
                        if last_msg.tool_calls:
                            print(f"\n[Narzędzie] Model chce użyć: {last_msg.tool_calls[0]['name']}")
                        elif last_msg.content:
                            print(f"\r\033[K", end="")
                            print(f"\nAsystent:\n{last_msg.content}")

                            # Generation metrics: the final answer of the turn
                            # (rag_generation_metrics)
                            _log_generation_metrics(
                                user_input,
                                str(last_msg.content),
                                turn_state.get("chars", 0),
                                t0,
                            )

            except KeyboardInterrupt:
                print("\nPrzerwano.")
                break
            except Exception as e:
                print(f"\nBłąd w pętli czatu: {e}")


if __name__ == "__main__":
    asyncio.run(run_chat_loop())