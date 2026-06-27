from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.models.request_model import TTSRequest
from app.services.tts_service import TTSService

router = APIRouter()


@router.post("/generate")
async def generate_audio(request: TTSRequest):

    result = await TTSService.generate_audio(
        request.text
    )

    if not result["success"]:

        raise HTTPException(
            status_code=500,
            detail=result["error"]
        )

    return FileResponse(
        path=result["file_path"],
        media_type="audio/mpeg",
        filename=result["filename"]
    )
