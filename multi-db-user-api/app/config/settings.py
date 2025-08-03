import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_URL = os.getenv("POSTGRES_URL")
    MONGO_URL = os.getenv("MONGO_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()
