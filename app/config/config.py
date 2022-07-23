import os

from pydantic import BaseSettings


class Configs(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT")
    database: str = os.getenv("DATABASE")
    database_port: str = os.getenv("DATABASE_PORT")
    database_username: str = os.getenv("DATABASE_USERNAME")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    database_host: str = os.getenv("DATABASE_HOST")
    is_file_logging_enabled: str = os.getenv("IS_FILE_LOGGING_ENABLED")
    is_system_logging_enabled: str = os.getenv("IS_SYSTEM_LOGGING_ENABLED")
    pool_recycle: int = int(os.getenv('POOL_RECYCLE') or 240)
    pool_timeout: int = int(os.getenv('POOL_TIMEOUT') or 30)
    pool_size: int = int(os.getenv('POOL_SIZE') or 50)
    max_overflow: int = int(os.getenv('MAX_OVERFLOW') or 10)


def get_configs() -> BaseSettings:
    return Configs()
