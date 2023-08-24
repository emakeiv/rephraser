from app.settings import settings
from fastapi.security import HTTPBearer
from app.common.parsers import ResponseParser
from app.clients.openai import OpenAiServiceClient
from app.clients.templates.template_manager import TemplateManager

"""
todo: convert to a dependencies factory class
"""

def get_openai_client() -> OpenAiServiceClient:
    return OpenAiServiceClient(key=settings.open_ai_key, model=settings.llm_model)

def get_template_manager() -> TemplateManager:
    return TemplateManager()

def get_response_parser() -> ResponseParser:
    return ResponseParser()

def get_security_schema() -> HTTPBearer:
    return HTTPBearer()

def get_common_dependencies():
    return [
        get_openai_client,
        get_template_manager,
        get_response_parser,
        get_security_schema,
    ]
