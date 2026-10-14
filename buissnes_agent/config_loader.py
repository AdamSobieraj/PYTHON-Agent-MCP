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
    """Singleton holding the application configuration."""
    _instance = None
    _data: Dict[str, Any] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _determine_profile(self) -> str:
        """
        Determines the profile in the following order:
        1. Command-line argument (--prof / --profile)
        2. Environment variable (APP_PROFILE)
        3. Default ('default')
        """
        # 1. Parse arguments (we use parse_known_args so it doesn't clash with the rest of the app)
        parser = argparse.ArgumentParser(add_help=False)  # add_help=False so we don't take over the -h flag
        parser.add_argument("--prof", "--profile", dest="profile", type=str, help="Configuration profile name")

        # Fetch the arguments, ignoring unknown ones (so the main app can keep its own flags)
        args, _ = parser.parse_known_args()

        if args.profile:
            logger.info(f"Wykryto profil z argumentów CLI: {args.profile}")
            return args.profile

        # 2. Check the environment variable
        env_profile = os.getenv("APP_PROFILE")
        if env_profile:
            logger.info(f"Wykryto profil ze zmiennej środowiskowej: {env_profile}")
            return env_profile

        # 3. Default
        return "default"

    def _load_config(self):
        """Loads configuration: default.yaml + {profile}.yaml + ENV overrides."""

        # 1. Determine the paths
        base_dir = os.path.dirname(os.path.abspath(__file__))  # buissnes_agent/
        project_root = os.path.dirname(base_dir)  # project root
        config_dir = os.path.join(project_root, "config")

        # 2. Determine the profile
        profile = self._determine_profile()
        logger.info(f"Ładowanie konfiguracji dla profilu: {profile}")

        # 3. Load DEFAULT
        default_path = os.path.join(config_dir, "default.yaml")
        self._data = self._load_yaml(default_path)

        # 4. Load PROFILE specific (override)
        if profile != "default":
            profile_path = os.path.join(config_dir, f"{profile}.yaml")
            profile_data = self._load_yaml(profile_path)
            self._merge_dicts(self._data, profile_data)

        # 5. Override from environment variables (optional, for Docker/K8s)
        self._apply_env_overrides()

        # 4. Override from CLI arguments (HIGHEST PRIORITY)
        self._apply_cli_overrides()

        logger.info("Konfiguracja załadowana pomyślnie.")

    def _apply_cli_overrides(self):
        """Reads CLI parameters that override the YAML/ENV configuration."""
        parser = argparse.ArgumentParser(add_help=False)
        # Register the CLI argument we care about
        parser.add_argument("--collection-name", type=str, help="Overrides the Qdrant collection name (from YAML)")

        ### Add a flag for the bucket
        parser.add_argument("--bucket", type=str, help="Overrides the S3 Bucket name")

        # We use parse_known_args to ignore the other flags provided by the user
        args, _ = parser.parse_known_args()

        if args.collection_name:
            logger.info(
                f"Wykryto argument CLI dla kolekcji. Nadpisywanie: vector_db.collection_name = '{args.collection_name}'")
            # Make sure the branch in the dict exists
            if "vector_db" not in self._data:
                self._data["vector_db"] = {}

            # Override the value in the configuration dict
            self._data["vector_db"]["collection_name"] = args.collection_name

        ### Save the bucket from CLI, if provided
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
        """Recursively merge dictionaries."""
        for k, v in override.items():
            if isinstance(v, dict) and k in base and isinstance(base[k], dict):
                self._merge_dicts(base[k], v)
            else:
                base[k] = v

    def _apply_env_overrides(self):
        """
        Allows overriding any key via ENV.
        Convention: APP__SECTION__KEY (double underscore is the separator)
        """
        prefix = "APP__"
        for env_key, env_val in os.environ.items():
            if env_key.startswith(prefix):
                # Strip the prefix and split on __
                keys = env_key[len(prefix):].lower().split("__")

                # Navigate deep into the dict
                target = self._data
                for k in keys[:-1]:
                    if k not in target:
                        target[k] = {}
                    target = target[k]

                # Set the value
                target[keys[-1]] = env_val
                logger.debug(f"Nadpisano z ENV: {keys} = {env_val}")

        ### Directly load S3_BUCKET from ENV (if present)
        s3_bucket_env = os.getenv("S3_BUCKET")
        if s3_bucket_env:
            if "s3" not in self._data:
                self._data["s3"] = {}
            self._data["s3"]["bucket"] = s3_bucket_env
            logger.info(f"Wykryto zmienną środowiskową S3_BUCKET. Ustawianie: s3.bucket = '{s3_bucket_env}'")

    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get a value from the configuration using dot notation.
        E.g. config.get("vector_db.collection_name")
        """
        keys = key_path.split(".")
        val = self._data
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val


_settings = None

def get_settings():
    global _settings
    if _settings is None:
        _settings = Config()
    return _settings