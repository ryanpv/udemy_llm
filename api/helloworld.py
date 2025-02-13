from fastapi import FastAPI

app = FastAPI()

@app.get("/first")
async def hello():
  return "Hello World"

# @app.get("/")

print("hello world")

@app.get("/")
async def homepage():
  return "This is the home page"