from app import dependencies
from fastapi.security import HTTPBearer
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import RephraseRequestSchema, RephraseResponseSchema

router = APIRouter()

@router.post("/rephrase", tags=["rephraser"], response_model=list[str])
async def process_phrase(
    request: RephraseRequestSchema,
    openai_client=Depends(dependencies.get_openai_client),
    template_manager=Depends(dependencies.get_template_manager),
    parser=Depends(dependencies.get_response_parser),
    token: str = Depends(dependencies.get_security_schema()),
):
    user_input = request.dict()
 
    try:
        promt = await template_manager.form_template(user_input, template_name="rephrase_template")
        generated = await openai_client.get_response(promt)
    except Exception:
        raise HTTPException(
            status_code=500, detail="An error occurred while processing your request"
        )
    response_data = parser.parse_response(generated[0], RephraseResponseSchema)
    return response_data.variants
