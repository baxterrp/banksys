from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="DB_",
        env_file=Path(__file__).resolve().parents[3] / ".env",
        extra="ignore"
    )

    host: str
    user: str
    password: SecretStr
    port: int
    name: str

    @property
    def url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name
        )

@lru_cache
def get_database_settings() -> DatabaseSettings:
    return DatabaseSettings() # pyright: ignore[reportCallIssue]

