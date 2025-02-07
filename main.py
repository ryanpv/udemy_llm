import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=OPENAI_KEY)

"""
completion = client.chat.completions.create(
  model='gpt-3.5-turbo',
  messages=[
    {"role":"system", "content":"You are a helpful assistant."},
    {"role":"user", "content":"Who is the current president of the United States?"}
  ]
)

print(completion.choices[0].message.content)
"""


speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="tts-1",
    voice="alloy",
    input="Everyday is a wonderful day to build something people love!",
) as response:
  with open(speech_file_path, 'wb') as f:
    for chunk in response.iter_bytes():
      f.write(chunk)

print(f"Speech file saved to {speech_file_path}")