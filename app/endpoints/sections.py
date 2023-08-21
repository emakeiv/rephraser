from app import dependencies
from fastapi import APIRouter, Depends
from app.schemas.models import (
    SectionRequestSchema,
    SectionResponseSchema
)

router = APIRouter()


@router.post("/generate-sections", tags=["section_content"], response_model=SectionResponseSchema)
async def generate_sections(
    req: SectionRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):  

    health_check = openai_client.get_heartbeat()
    if health_check:
        generated_content = {}
        for section_name, section_data in req.sections.items():
            print(section_name, section_data)

        return generated_content
