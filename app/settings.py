from pydantic import BaseSettings


class Settings(BaseSettings):
    """The configuration that will be used by the application."""

    API_V1_STR: str = "/api/v1"


settings = Settings()
