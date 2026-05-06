import logging
import os
import sys

from dotenv import load_dotenv

from QdrantDatabaseStore import QdrantDatabaseStore
from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.config_loader import get_settings

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

load_dotenv()

KNOWLEDGE_BASE = None


def get_knowledge_base():
    """
    Singleton Pattern: Tworzy lub zwraca istniejącą instancję SearchKnowledgebase.
    Odpowiada za wstrzyknięcie zależności (Client, Store, Config).
    """
    settings = get_settings()

    global KNOWLEDGE_BASE
    if KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE
    # Lazy import - zapobiega błędom cyklicznego importu
    from KnowledgebasePipeline import SearchKnowledgebase
    # 1. Konfiguracja Chunkera
    data_source = settings.get("data_source.type")
    # 2. Konfiguracja Wymiaru Embeddings
    # OpenAI text-embedding-3-small/large = 1536, Nomic/Titan = 768
    try:
        emb_dim = int(os.getenv("EMBEDDING_DIM"))
    except (TypeError, ValueError):
        emb_dim = 1536
    # =========================================================
    # DYNAMICZNY IMPORT LOADERA (Warstwa Danych)
    # =========================================================
    # Importujemy klasę dopiero tutaj, wewnątrz IF-a.
    # Dzięki temu nie musimy mieć boto3, jeśli używamy 'local'.
    if data_source == "s3":
        logger.info("Dynamic Import: Ladowanie modulu S3...")
        from DataLoaderS3FileLoader import DataLoaderS3FileLoader

        data_loader = DataLoaderS3FileLoader(
            bucket_name=settings.get("s3.bucket"),
            prefix=settings.get("data_s3_source.input_path"),
        )
    else:
        logger.info("Dynamic Import: Ladowanie modulu LocalFile...")
        # Import wewnątrz funkcji!
        from DataLoaderLocalFileLoader import DataLoaderLocalFileLoader

        data_loader = DataLoaderLocalFileLoader(
            directory=settings.get("data_source.local_input_path")
        )
    # 3. Inicjalizacja Klientów
    embedding_client = LocalEmbeddingClient()

    store = QdrantDatabaseStore(
        url=os.getenv("QDRANT_API"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=settings.get("vector_db.collection_name"),
        vector_size=emb_dim,
    )
    # 4. Instancjalizacja Głównego Orkiestratora
    KNOWLEDGE_BASE = SearchKnowledgebase(
        client=embedding_client,
        database_store=store,
        data_loader=data_loader,
        embedding_model=os.getenv("EMBEDDING_MODEL"),
        force_refresh=False, # Ustaw True w .env lub tutaj, aby wymusić przeładowanie bazy
    )
    return KNOWLEDGE_BASE


try:
    get_knowledge_base()
except Exception as exc:
    logger.exception(
        "CRITICAL INIT ERROR: Nie udalo sie zainicjalizowac bazy wiedzy: %s",
        exc,
    )
    raise
