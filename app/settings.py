import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT")
    testing: bool = os.getenv("TESTING")
    database_url: str = os.getenv("DATABASE_URL")
    open_ai_key: str = os.getenv("OPEN_AI_KEY")
    auth_sec: str = os.getenv("AUTH_SECRET")
    auth_alg: str = os.getenv("AUTH_ALGO")

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
