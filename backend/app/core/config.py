from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Example fields
    API_KEY: str = Field(..., env="API_KEY")
    DEBUG: bool = Field(False, env="DEBUG")

    # If you need .env files or other config
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
