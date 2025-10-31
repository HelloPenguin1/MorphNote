from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str 


class stylizeRequest(BaseModel):
    text: str
    style: str
    options: dict = None