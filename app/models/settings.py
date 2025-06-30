from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    app_name: str = "Intelligent Agent API"
    allowed_origins: List[str] = ["*"]
    weather_api_key: str = ""
    openai_api_key: str = ""  # For OpenAI and evaluation judge
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

    class Config:
        env_file = ".env"

settings = Settings()