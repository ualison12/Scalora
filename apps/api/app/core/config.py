from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Scalora API"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    API_PREFIX: str = "/api/v1"

    # Variáveis do banco de dados (mapeadas para aceitar o seu .env)
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "secret"
    POSTGRES_DB: str = "scalora_db"
    POSTGRES_PORT: str = "5432"
    POSTGRES_HOST: str = "localhost"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"  # Se tiver mais alguma variável perdida no .env, ele ignora silenciosamente em vez de quebrar
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()