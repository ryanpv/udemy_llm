import io
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from openai import OpenAI

router = APIRouter()
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

@router.post("/api/audio/tts")
async def tts():
  response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input="hello world, i am ryan"
  )

  audio_byte = io.BytesIO(response.content) # streaming the binary response

  return StreamingResponse(audio_byte, media_type="audio/mp3")