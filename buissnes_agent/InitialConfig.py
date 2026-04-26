import logging
import os
import sys

from dotenv import load_dotenv

from QdrantDatabaseStore import QdrantDatabaseStore
from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.config_loader import settings

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

load_dotenv()

KNOWLEDGE_BASE = None


def get_knowledge_base():
    """
    Singleton factory for the knowledge-base pipeline.
    """
    global KNOWLEDGE_BASE
    if KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE

    from KnowledgebasePipeline import SearchKnowledgebase

    data_source = settings.get("data_source.type")

    try:
        emb_dim = int(os.getenv("EMBEDDING_DIM"))
    except (TypeError, ValueError):
        emb_dim = 1536

    if data_source == "s3":
        logger.info("Dynamic Import: Ladowanie modulu S3...")
        from DataLoaderS3FileLoader import DataLoaderS3FileLoader

        data_loader = DataLoaderS3FileLoader(
            bucket_name=settings.get("s3.bucket"),
            prefix=settings.get("data_s3_source.input_path"),
        )
    else:
        logger.info("Dynamic Import: Ladowanie modulu LocalFile...")
        from DataLoaderLocalFileLoader import DataLoaderLocalFileLoader

        data_loader = DataLoaderLocalFileLoader(
            directory=settings.get("data_source.local_input_path")
        )

    embedding_client = LocalEmbeddingClient()

    store = QdrantDatabaseStore(
        url=os.getenv("QDRANT_API"),
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=settings.get("vector_db.collection_name"),
        vector_size=emb_dim,
    )

    KNOWLEDGE_BASE = SearchKnowledgebase(
        client=embedding_client,
        database_store=store,
        data_loader=data_loader,
        embedding_model=os.getenv("EMBEDDING_MODEL"),
        force_refresh=False,
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
