from fastapi import FastAPI
from models.schemas import TextRequest

app = FastAPI(
    title="MorphNote",
    description="AI-Assisted Notes App using Generative AI",
    version="1.0.0"
)


