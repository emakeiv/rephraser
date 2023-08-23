from app.settings import settings
from app.common.parsers import ResponseParser
from app.clients.openai import OpenAiServiceClient
from app.clients.templates.template_manager import TemplateManager
from app.clients.templates.template_preprocessor import TemplatePreprocessor

def get_openai_client() -> OpenAiServiceClient:
    return OpenAiServiceClient(
        key=settings.open_ai_key, 
        model=settings.llm_model
        )

def get_template_manager() -> TemplateManager:
    return TemplateManager()

def get_template_preprocessor() -> TemplatePreprocessor:
    return TemplatePreprocessor()

def get_response_parser() -> ResponseParser:
    return ResponseParser()
