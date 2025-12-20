from fastapi import FastAPI
from router.security_router import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
async def root():
    return {"root": "healthy"}