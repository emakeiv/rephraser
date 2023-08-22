from pydantic import BaseModel, Field, validator


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
    variants: list[str]


class SectionSchema(BaseModel):
    title: int | None = None
    subtitle: int | None = None
    description: int | None = None


class SectionRequestSchema(BaseModel):
    description: str = Field(..., min_length=1, description="User business description")
    sections: dict[str, SectionSchema]

    @validator("sections", pre=True, always=True)
    def filter_empty_sections(cls, value):
        return {
            section_name: section_data
            for section_name, section_data in value.items()
            if any(
                component is not None and isinstance(component, int)
                for component in section_data.values()
            )
        }

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
