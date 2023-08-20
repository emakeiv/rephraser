from pydantic import BaseModel

class RephraseRequestSchema(BaseModel):
    text: str
    number_of_variants: int

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Sample of text to be rephrased",
                "number_of_variants": 2
            }
        }

class RephraseResponseSchema(BaseModel):
    variants: list[str]

class SectionSchema(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    description: list[str] | None = None

class SectionRequestSchema(BaseModel):
    description: str
    sections: dict[str, SectionSchema]

class SectionResponseSchema(BaseModel):
    title: str
    subtitle: str | None = None
    description: list[str] | None = None





