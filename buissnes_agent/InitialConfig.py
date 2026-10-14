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
    Singleton Pattern: Creates or returns the existing SearchKnowledgebase instance.
    Responsible for dependency injection (Client, Store, Config).
    """
    settings = get_settings()

    global KNOWLEDGE_BASE
    if KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE
    # Lazy import - prevents circular import errors
    from KnowledgebasePipeline import SearchKnowledgebase
    # 1. Chunker configuration
    data_source = settings.get("data_source.type")
    # 2. Embedding dimension configuration
    # OpenAI text-embedding-3-small/large = 1536, Nomic/Titan = 768
    try:
        emb_dim = int(os.getenv("EMBEDDING_DIM"))
    except (TypeError, ValueError):
        emb_dim = 1536
    # =========================================================
    # DYNAMIC LOADER IMPORT (Data Layer)
    # =========================================================
    # The class is imported only here, inside the IF block.
    # This way we don't need boto3 when using 'local'.
    if data_source == "s3":
        logger.info("Dynamic Import: Ladowanie modulu S3...")
        from DataLoaderS3FileLoader import DataLoaderS3FileLoader

        data_loader = DataLoaderS3FileLoader(
            bucket_name=settings.get("s3.bucket"),
            prefix=settings.get("data_s3_source.input_path"),
        )
    else:
        logger.info("Dynamic Import: Ladowanie modulu LocalFile...")
        # Import inside the function!
        from DataLoaderLocalFileLoader import DataLoaderLocalFileLoader

        data_loader = DataLoaderLocalFileLoader(
            directory=settings.get("data_source.local_input_path")
        )
    # 3. Client initialization
    embedding_client = LocalEmbeddingClient()

    store = QdrantDatabaseStore(
        url=os.getenv("QDRANT_API"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=settings.get("vector_db.collection_name"),
        vector_size=emb_dim,
    )
    # 4. Initialization of the Main Orchestrator
    KNOWLEDGE_BASE = SearchKnowledgebase(
        client=embedding_client,
        database_store=store,
        data_loader=data_loader,
        embedding_model=os.getenv("EMBEDDING_MODEL"),
        force_refresh=False, # Set True in .env or here to force a database reload
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
