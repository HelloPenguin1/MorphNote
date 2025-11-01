from fastapi import FastAPI
from models.schemas import TextRequest, stylizeRequest
from chains.keypoints_chain import extract_keypoints
from chains.stylization_chain import stylize_text
from chains.summarization_chain import summarize_text_notes

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
        options=req.options.dict() if req.options else {}
    )
    return {"stylized_text": result}

@app.post("/summarize_text")
async def summarize(req: TextRequest):
    summary = summarize_text_notes(req.text)
    return {"summary": summary}