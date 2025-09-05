"""Type hints for environment variables."""
from dataclasses import dataclass


@dataclass
class Settings:
    ENVIRONMENT: str
    SECRET_KEY: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
