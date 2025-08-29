import os

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    JSON_SORT_KEYS = False  # To preserve the order of JSON responses


class DevelopmentConfig(BaseConfig):
    DEBUG = True   # Enable debug mode for development


class TestingConfig(BaseConfig):
    TESTING = True  # Enable testing mode
    SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///:memory:"


class ProductionConfig(BaseConfig):
    DEBUG = False


CONFIG_MAP = {
"development": DevelopmentConfig,
"testing": TestingConfig,
"production": ProductionConfig,
}


def get_config():
    env = os.getenv("APP_ENV", "development").lower()
    return CONFIG_MAP.get(env, DevelopmentConfig)