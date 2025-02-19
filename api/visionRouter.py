import os

from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

router = APIRouter()
OPENAI_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

@router.post("/api/vision/imggeneration")
async def image_generation(image_prompt: str):
  response = client.images.generate(
    model="dall-e-3",
    prompt=image_prompt,
    size="1024x1024",
    quality="standard",
    n=1
  )

  return response.data[0].url
