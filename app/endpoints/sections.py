from fastapi import APIRouter
from fastapi import Request
from app.schemas.models import (
    SectionRequestSchema, 
    SectionResponseSchema,
    SectionSchema,
    
)

router = APIRouter()

@router.post("/generate-sections",  tags=["section_content"])
async def generate_sections(request:SectionRequestSchema):
    generated_content = {}
    return generated_content

