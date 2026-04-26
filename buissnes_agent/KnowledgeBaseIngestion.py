import logging
import sys

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger("ETL-Process")

load_dotenv()


def main():
    logger.info("=== ROZPOCZYNAM PROCES INGESTII DANYCH (ETL) ===")

    try:
        import InitialConfig

        InitialConfig.get_knowledge_base()
        print("[Server] Konfiguracja ETL zaladowana pomyslnie.", file=sys.stderr)
        logger.info("=== PROCES INGESTII ZAKONCZONY SUKCESEM ===")
    except Exception as exc:
        logger.error("BLAD KRYTYCZNY PODCZAS INGESTII: %s", exc)
        print(
            f"[Server] Ostrzezenie: Blad podczas ladowania ETL: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
