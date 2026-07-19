from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError

class Settings(BaseSettings):
    PROJECT_NAME: str = "Scalora API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database Settings
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432

    # Configuração para ler o arquivo .env
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

settings = Settings()