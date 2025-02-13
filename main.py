from fastapi import FastAPI

from api.textRouter import router as textRouter

app = FastAPI()

app.include_router(textRouter)