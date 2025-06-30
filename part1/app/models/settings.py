from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

class Settings(BaseSettings):
    pp_name: str = "Intelligent Agent API"
    allowed_origins: list = ["*"]
    
    # These will now be properly loaded from .env
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    weather_api_key: str = os.getenv("WEATHER_API_KEY", "") # For OpenAI and evaluation judge
    system_prompt: str = """
    You are a helpful, creative, and precise AI assistant. Follow these guidelines:
    1. Be friendly but professional in tone
    2. If a query is unclear, ask clarifying questions
    3. For off-topic or inappropriate requests, respond politely but firmly
    4. When using tools, be transparent about the source
    5. Always verify facts before responding
    6. If unsure, say you don't know rather than guessing
    """
    fallback_prompt: str = "I'm sorry, I couldn't process your request. Could you please rephrase or provide more details?"
   
   
settings = Settings()

print(f"[DEBUG] OpenAI key loaded: {bool(settings.openai_api_key)}")
print(f"[DEBUG] Weather key loaded: {bool(settings.weather_api_key)}")