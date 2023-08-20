from app.clients.openai import OpenAiServiceClient




def get_openai_client() -> OpenAiServiceClient:
    openai_service_parameters = {
        'key': "blabla",
        'model': 'gpt-3.5.turbo', 
        'top_p': 1,
        'n': 1
    }
    return OpenAiServiceClient(**openai_service_parameters)