from pydantic import BaseModel, Field


class RephraseRequestSchema(BaseModel):
    text: str = Field(..., min_length=1, description="Text to be rephrased")
    number_of_variants: int = Field(
        ..., gt=0, description="Number of rephrased variants"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Brown fox jumps over the lazy dog",
                "number_of_variants": 2,
            }
        }


class RephraseResponseSchema(BaseModel):
    original_text: str
    variants: list[str] = None


class SectionSchema(BaseModel):
    title: int | None = None
    subtitle: int | None = None
    description: int | None = None


class SectionRequestSchema(BaseModel):
    description: str = Field(..., min_length=1, description="User business description")
    sections: dict[str, SectionSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "description": "Company sales quality cofins because death is always in demand",
                "sections": {
                    "about": {"title": 1, "description": 2},
                    "refunds": {"title": 1, "description": 1},
                    "hero": {"title": 1, "subtitle": 1},
                },
            }
        }


class SectionResponseSchema(BaseModel):
    title: str
    subtitle: str | None = None
    description: list[str] | str = None
