from app import dependencies
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.models import RephraseRequestSchema, RephraseResponseSchema
from app.common.parsers import ResponseParser

router = APIRouter()
parser = ResponseParser()

@router.post("/rephrase", tags=["rephraser"], response_model=list[str])
async def process_phrase(
    request: RephraseRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):  
    user_input = request.dict()
    try:
        rephrased_phrase = await openai_client.get_response(user_input, template_name="rephrase_template")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing your request")
    response_data = parser.parse_response(rephrased_phrase[0], RephraseResponseSchema)
    return response_data.variants   


