import os
import sys
import yaml
import logging
import argparse
from typing import Any, Dict
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ConfigLoader")
load_dotenv()
class Config:
    """Singleton przechowujący konfigurację aplikacji."""
    _instance = None
    _data: Dict[str, Any] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _determine_profile(self) -> str:
        """
        Ustala profil w kolejności:
        1. Argument linii poleceń (--prof / --profile)
        2. Zmienna środowiskowa (APP_PROFILE)
        3. Domyślny ('default')
        """
        # 1. Parsowanie argumentów (używamy parse_known_args, żeby nie gryzło się z resztą aplikacji)
        parser = argparse.ArgumentParser(add_help=False)  # add_help=False, by nie przejmować flagi -h
        parser.add_argument("--prof", "--profile", dest="profile", type=str, help="Nazwa profilu konfiguracyjnego")

        # Pobieramy argumenty, ignorując nieznane (żeby główna aplikacja mogła mieć swoje flagi)
        args, _ = parser.parse_known_args()

        if args.profile:
            logger.info(f"Wykryto profil z argumentów CLI: {args.profile}")
            return args.profile

        # 2. Sprawdzenie zmiennej środowiskowej
        env_profile = os.getenv("APP_PROFILE")
        if env_profile:
            logger.info(f"Wykryto profil ze zmiennej środowiskowej: {env_profile}")
            return env_profile

        # 3. Domyślny
        return "default"

    def _load_config(self):
        """Ładuje konfigurację: default.yaml + {profile}.yaml + ENV overrides."""

        # 1. Określenie ścieżek
        base_dir = os.path.dirname(os.path.abspath(__file__))  # buissnes_agent/
        project_root = os.path.dirname(base_dir)  # root projektu
        config_dir = os.path.join(project_root, "config")

        # 2. Ustalenie profilu
        profile = self._determine_profile()
        logger.info(f"Ładowanie konfiguracji dla profilu: {profile}")

        # 3. Ładowanie DEFAULT
        default_path = os.path.join(config_dir, "default.yaml")
        self._data = self._load_yaml(default_path)

        # 4. Ładowanie PROFILE specific (nadpisanie)
        if profile != "default":
            profile_path = os.path.join(config_dir, f"{profile}.yaml")
            profile_data = self._load_yaml(profile_path)
            self._merge_dicts(self._data, profile_data)

        # 5. Nadpisanie ze zmiennych środowiskowych (opcjonalne, dla Docker/K8s)
        self._apply_env_overrides()

        # 4. Nadpisanie z argumentów CLI (NAJWYŻSZY PRIORYTET)
        self._apply_cli_overrides()

        logger.info("Konfiguracja załadowana pomyślnie.")

    def _apply_cli_overrides(self):
        """Pobiera parametry z CLI, które nadpisują konfigurację w YAML/ENV."""
        parser = argparse.ArgumentParser(add_help=False)
        # Rejestrujemy argument CLI, który nas interesuje
        parser.add_argument("--collection-name", type=str, help="Nadpisuje nazwę kolekcji Qdrant (z YAML)")

        ### Dodajemy flagę dla bucketa
        parser.add_argument("--bucket", type=str, help="Nadpisuje nazwę S3 Bucket")

        # Używamy parse_known_args, żeby zignorować inne flagi podane przez użytkownika
        args, _ = parser.parse_known_args()

        if args.collection_name:
            logger.info(
                f"Wykryto argument CLI dla kolekcji. Nadpisywanie: vector_db.collection_name = '{args.collection_name}'")
            # Upewniamy się, że gałąź w słowniku istnieje
            if "vector_db" not in self._data:
                self._data["vector_db"] = {}

            # Nadpisujemy wartość w słowniku konfiguracyjnym
            self._data["vector_db"]["collection_name"] = args.collection_name

        ### Zapisujemy bucket z CLI, jeśli został podany
        if args.bucket:
            logger.info(f"Wykryto argument CLI dla S3. Nadpisywanie: s3.bucket = '{args.bucket}'")
            if "s3" not in self._data:
                self._data["s3"] = {}
            self._data["s3"]["bucket"] = args.bucket

    def _load_yaml(self, path: str) -> Dict:
        if not os.path.exists(path):
            logger.warning(f"Plik konfiguracyjny nie istnieje: {path}")
            return {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            logger.error(f"Błąd parsowania YAML {path}: {e}")
            return {}

    def _merge_dicts(self, base: Dict, override: Dict):
        """Rekurencyjne łączenie słowników."""
        for k, v in override.items():
            if isinstance(v, dict) and k in base and isinstance(base[k], dict):
                self._merge_dicts(base[k], v)
            else:
                base[k] = v

    def _apply_env_overrides(self):
        """
        Umożliwia nadpisywanie dowolnego klucza przez ENV.
        Konwencja: APP__SECTION__KEY (podwójne podkreślenie to separator)
        """
        prefix = "APP__"
        for env_key, env_val in os.environ.items():
            if env_key.startswith(prefix):
                # Usuwamy prefix i dzielimy po __
                keys = env_key[len(prefix):].lower().split("__")

                # Nawigujemy w głąb słownika
                target = self._data
                for k in keys[:-1]:
                    if k not in target:
                        target[k] = {}
                    target = target[k]

                # Ustawiamy wartość
                target[keys[-1]] = env_val
                logger.debug(f"Nadpisano z ENV: {keys} = {env_val}")

        bucket_env_candidates = [
            ("S3_BUCKET", os.getenv("S3_BUCKET")),
            ("S3_BUCKET_CONTAINER", os.getenv("S3_BUCKET_CONTAINER")),
            ("S3_BUCKET_NAME", os.getenv("S3_BUCKET_NAME")),
            ("AWS_S3_BUCKET", os.getenv("AWS_S3_BUCKET")),
        ]
        bucket_env_name = None
        s3_bucket_env = None
        for candidate_name, candidate_value in bucket_env_candidates:
            if candidate_value:
                bucket_env_name = candidate_name
                s3_bucket_env = candidate_value
                break

        if s3_bucket_env:
            if "s3" not in self._data:
                self._data["s3"] = {}
            self._data["s3"]["bucket"] = s3_bucket_env
            logger.info(
                f"Wykryto zmienną środowiskową {bucket_env_name}. "
                f"Ustawianie: s3.bucket = '{s3_bucket_env}'"
            )

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Pobiera wartość z konfiguracji używając notacji kropkowej.
        Np. config.get("vector_db.collection_name")
        """
        keys = key_path.split(".")
        val = self._data
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val


# Globalna instancja
settings = Config()
