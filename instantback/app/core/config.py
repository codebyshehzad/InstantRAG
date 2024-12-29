# File: app/core/config.py
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

class Settings(BaseSettings):
    # Load sensitive data from .env
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "instantrag")  # Default value if not in .env
    PINECONE_HOST: str = os.getenv("PINECONE_HOST")  # Added for Pinecone host
    PINECONE_REGION: str = os.getenv("PINECONE_REGION", "us-east-1")  # Default region
    VECTOR_DIMENSION: int = int(os.getenv("VECTOR_DIMENSION", 384))  # Default vector dimension

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")  # Default database URL

    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")  # Replace with a strong key in .env
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")  # JWT algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))  # Token expiration time

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a settings instance to access the variables
settings = Settings()
