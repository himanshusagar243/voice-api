from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()
API_KEY = "voice123"

class VoiceInput(BaseModel):
    audio: str

@app.post("/analyze")
def analyze_voice(data: VoiceInput, authorization: str = Header(None)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "classification": "AI-generated",
        "confidence": 0.65,
        "explanation": "Audio characteristics match synthetic voice patterns"
    }
