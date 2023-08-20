
from fastapi import APIRouter
from fastapi import Request
from app.schemas.response_schemas import (
    RephraseRequestSchema,
    RephraseResponseSchema,
    SectionRequestSchema, 
    SectionResponseSchema,
    SectionSchema,
    
)

router = APIRouter()

@router.post("/rephrase", tags=["rephraser"])
async def process_phrase(request: RephraseRequestSchema):
    return {"info": "end point for rephrase feature"}

@router.post("/sections", response_model=SectionResponseSchema, alias="section-content", tags=["section_content"])
async def generate_sections(request:SectionRequestSchema):
    return {"info": "end point for generated sections"}

