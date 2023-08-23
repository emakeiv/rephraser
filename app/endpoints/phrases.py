from app import dependencies
from fastapi.security import HTTPBearer
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import RephraseRequestSchema, RephraseResponseSchema

router = APIRouter()
security_schema = HTTPBearer()


@router.post("/rephrase", tags=["rephraser"], response_model=list[str])
async def process_phrase(
    request: RephraseRequestSchema,
    openai_client=Depends(dependencies.get_openai_client),
    template_manager=Depends(dependencies.get_template_manager),
    template_preprocessor=Depends(dependencies.get_template_preprocessor),
    parser=Depends(dependencies.get_response_parser),
    token: str = Depends(security_schema),
):
    user_input = request.dict()
    try:
        template = await template_manager.get_template(
            template_name="rephrase_template"
        )
        promt = template_preprocessor.preprocess_template(user_input, template)
        generated = await openai_client.get_response(promt)
    except Exception:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing your request"
        )
    response_data = parser.parse_response(generated[0], RephraseResponseSchema)
    return response_data.variants
