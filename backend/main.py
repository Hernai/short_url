from fastapi import FastAPI
from routes.short_url import short

app = FastAPI(
        title='Shortener Url',
        description='Shortener Url with FastAPI + mongoDB',
        version=0.1)

app.include_router(short)

@app.get("/")
async def root():
    return {"message": "Hello World"}