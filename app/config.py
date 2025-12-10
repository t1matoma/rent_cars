from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DB_URL: str = os.getenv("DB_URL", "postgresql://postgres:postgres123@db:5432/rent_db")
    
    CORS_ORIGINS: list = ["http://localhost:3000"]
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore"
    }
    

@lru_cache
def get_settings():
    return Settings()