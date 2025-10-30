from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(description="Reference notes provided as input by the user")