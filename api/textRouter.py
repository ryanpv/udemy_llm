
import os

from dotenv import load_dotenv
from fastapi import APIRouter
from openai import OpenAI

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_KEY)

router = APIRouter()

@router.post("/api/text/chat")
async def chatinput(message: str):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": message}
    ]
  )

  return completion.choices[0].message.content

@router.post("/api/text/moderations")
async def moderation(textmoderation: str):
  response = client.moderations.create(
    model="omni-moderation-latest",
    input=textmoderation,
  )

  return response
