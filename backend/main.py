from fastapi import FastAPI
from models.schemas import TextRequest
from chains.keypoints_chain import extract_keypoints

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