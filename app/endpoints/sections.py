from app import dependencies
from fastapi.security import HTTPBearer
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import SectionRequestSchema, SectionResponseSchema

router = APIRouter()

@router.post(
    "/generate-sections",
    tags=["sections"],
    response_model=dict[str, SectionResponseSchema],
    response_model_exclude_none=True,
)
async def generate_sections(
    request: SectionRequestSchema,
    openai_client=Depends(dependencies.get_openai_client),
    template_manager=Depends(dependencies.get_template_manager),
    parser=Depends(dependencies.get_response_parser),
    token: str = Depends(dependencies.get_security_schema())
):
    user_input = request.dict()
    try:
        promt = await template_manager.form_template(user_input, template_name="generate_section_template")
        generated = await openai_client.get_response(promt)
    except Exception:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing your request"
        )
    response_data = parser.parse_response(generated[0], SectionResponseSchema)
    return response_data
