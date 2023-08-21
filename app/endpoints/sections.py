from app import dependencies
from fastapi import APIRouter, Depends
from app.schemas.models import (
    SectionRequestSchema, 
    SectionResponseSchema,
    SectionSchema,
    
)

router = APIRouter()

@router.post("/generate-sections",  tags=["section_content"])
async def generate_sections(
    req:SectionRequestSchema,
    openai_client = Depends(dependencies.get_openai_client)
    ):

    generated_content = {}
    for section_name, section_data in req.sections.items():
        print(section_name, section_data)

    return generated_content

