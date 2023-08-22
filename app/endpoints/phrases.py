from app import dependencies
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import RephraseRequestSchema, RephraseResponseSchema

router = APIRouter()


@router.post("/rephrase", tags=["rephraser"])
async def process_phrase(
    request: RephraseRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):  
    user_input = request.dict()
    try:
        rephrased_phrase = await openai_client.get_response(user_input, template_name="rephrase_template")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing your request")

    return {"temporary route response ": "ok"}
    return rephrased_phrase


