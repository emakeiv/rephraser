from fastapi import APIRouter
from fastapi import Request, Depends
from app import dependencies

from app.schemas.models import (
    RephraseRequestSchema,
    RephraseResponseSchema,   
)

router  = APIRouter()

@router.post("/rephrase", tags=["rephraser"])
async def process_phrase(req: RephraseRequestSchema, openai_service_client = Depends(dependencies.get_openai_client)):
    print(req.text)
    rephrased_variants = openai_service_client.get_response(req.text)
    return rephrased_variants


