from app import dependencies
from fastapi import APIRouter, Depends
from app.schemas.models import RephraseRequestSchema

router = APIRouter()


@router.post("/rephrase", tags=["rephraser"], response_model=list[str])
async def process_phrase(
    req: RephraseRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):
    rephrased_phrase = openai_client.get_response(
        user_input=req.text, variants=req.number_of_variants
    )

    return rephrased_phrase
