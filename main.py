
from app.server import create_server
from openai.service import OpenAiServiceClient 

openai_service_parameters = {
    'model': 'gpt-3.5.turbo', 
    'top_p': 1,
    'n': 1
}

openai_client = OpenAiServiceClient(**openai_service_parameters)
server = create_server()
