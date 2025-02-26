from fastapi import FastAPI

from api.audioRouter import router as audioRouter
from api.textRouter import router as textRouter
from api.visionRouter import router as visionRouter

app = FastAPI()

app.include_router(textRouter)
app.include_router(visionRouter)
app.include_router(audioRouter)