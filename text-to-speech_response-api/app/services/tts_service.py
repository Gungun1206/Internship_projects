from gtts import gTTS
import uuid
import os

AUDIO_DIR = "audio"

os.makedirs(AUDIO_DIR, exist_ok=True)


class TTSService:

    @staticmethod
    async def generate_audio(text: str):

        try:

            if not text.strip():

                return {
                    "success": False,
                    "error": "Text cannot be empty"
                }

            filename = f"{uuid.uuid4()}.mp3"

            filepath = os.path.join(
                AUDIO_DIR,
                filename
            )

            tts = gTTS(
                text=text,
                lang="en"
            )

            tts.save(filepath)

            return {
                "success": True,
                "file_path": filepath,
                "filename": filename
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }
