from app.settings import settings
from app.clients.openai import OpenAiServiceClient


def get_openai_client() -> OpenAiServiceClient:
    return OpenAiServiceClient(settings.open_ai_key)
