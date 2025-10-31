from fastapi import FastAPI
from models.schemas import TextRequest, stylizeRequest
from chains.keypoints_chain import extract_keypoints
from chains.stylization_chain import stylize_text

app = FastAPI(
    title="MorphNote",
    description="AI-Assisted Notes App using Generative AI",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to MorphNote",
    }


@app.post("/keypoints")
async def keypoints(req: TextRequest):
    points = extract_keypoints(req.text)
    return {"keypoints": points}


@app.post("/stylize")
async def stylize(req: stylizeRequest):
    result = stylize_text(
        text=req.text,
        style=req.style,
        options=req.options or {}
    )
    return {"stylized_text": result}