import os

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite+pysqlite:///:memory:")
    JSON_SORT_KEYS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
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