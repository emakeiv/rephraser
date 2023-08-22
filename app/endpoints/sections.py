from app import dependencies
from fastapi import APIRouter, Depends
from app.schemas.models import SectionRequestSchema, SectionResponseSchema
from app.common.parsers import ResponseParser

router = APIRouter()
parser = ResponseParser()

@router.post(
    "/generate-sections", 
    tags=["sections"], 
    response_model=dict[str,SectionResponseSchema],
    response_model_exclude_none=True
)
async def generate_sections(
    request: SectionRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):
    user_input = request.dict()
    try:
        generated_sections = await openai_client.get_response(user_input, template_name="generate_section_template")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing your request")

    response_data = parser.parse_response(generated_sections[0], SectionResponseSchema)
    return response_data
