import asyncio
from app import dependencies
from fastapi import APIRouter, Depends
from app.schemas.models import SectionRequestSchema, SectionResponseSchema

router = APIRouter()

# {
#       "description": "User business decription",
#       "sections": [
#             "about": {
#                   "title": 1,
#                   "description": 2
#             },
#             "refunds": {
#                   "title": 1,
#                   "description": 1
#             },
#             "hero": {
#                   "title": 1,
#                   "subtitle": 1
#             }
#       ]
# }


@router.post(
    "/generate-sections", tags=["section_content"], response_model=SectionResponseSchema
)
async def generate_sections(
    req: SectionRequestSchema, openai_client=Depends(dependencies.get_openai_client)
):
    async def generate_section(section_name, section_data):
        generated_content = {}

        async def generate_section(section_name, section_data):
            generated_variants = openai_client.get_response(
                user_input=section_data.description, variants=section_data.title
            )
            generated_content[section_name] = generated_variants

        tasks = [
            generate_section(section_name, section_data)
            for section_name, section_data in req.sections.items()
        ]

        await asyncio.gather(*tasks)

        return generated_content


# {
#       "about":{
#             "title": "About us",
#             "description": [
#                   "We do something",
#                   "Developing unique products"
#             ]
#       },
#       "refunds":{
#             "title": "Information about refund",
#             "description": "I want to know more"
#       },
#       "hero":{
#             "title": "Unique product development and other cool stuf",
#             "subtitle": "The use of quartz sand is a thing"
#       }
# }
