from app import dependencies
from fastapi.security import HTTPBearer
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import SectionRequestSchema, SectionResponseSchema

router = APIRouter()
security_schema = HTTPBearer()
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
    template_preprocessor=Depends(dependencies.get_template_preprocessor),
    parser=Depends(dependencies.get_response_parser),
    token:str=Depends(security_schema)
    
):
    user_input = request.dict()

    try:
        template = await template_manager.get_template(
            template_name="generate_section_template"
        )
        promt = template_preprocessor.preprocess_template(user_input, template)
        generated_sections = await openai_client.get_response(promt)
    except Exception:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing your request"
        )

    response_data = parser.parse_response(generated_sections[0], SectionResponseSchema)
    return response_data
