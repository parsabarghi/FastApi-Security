from fastapi import FastAPI
from contextlib import asynccontextmanager
from router.security_router import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"root": "healthy"}