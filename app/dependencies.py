from app.clients.openai import OpenAiServiceClient


def get_openai_client() -> OpenAiServiceClient:
    return OpenAiServiceClient()
