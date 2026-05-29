from fastapi import FastAPI
from app.routes.tts_routes import router

app = FastAPI(
    title="Text To Speech Response API",
    version="1.0.0"
)

app.include_router(router, prefix="/tts")


@app.get("/")
async def home():

    return {
        "message": "TTS API Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }
