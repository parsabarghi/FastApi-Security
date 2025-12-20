import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    DB_URL: str = os.getenv("DB_URL")


    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()