from openai import AsyncOpenAI
from app.models.schemas import ToolResponse, ToolType
from app.models.settings import settings
import logging

logger = logging.getLogger(__name__)

class OpenAITool:
    def __init__(self):
        logger.info(f"Initializing OpenAI with key: {settings.openai_api_key[:5]}...")
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def generate_content(self, prompt: str, system_prompt: str = "") -> ToolResponse:
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )
            
            return ToolResponse(
                tool_type=ToolType.OPENAI,
                content={
                    "text": response.choices[0].message.content,
                    "usage": {
                        "prompt_tokens": response.usage.prompt_tokens,
                        "completion_tokens": response.usage.completion_tokens,
                        "total_tokens": response.usage.total_tokens
                    }
                },
                success=True
            )
        except Exception as e:
            logger.error(f"OpenAI error: {str(e)}")
            return ToolResponse(
                tool_type=ToolType.OPENAI,
                content={},
                success=False,
                error_message=str(e)
            )