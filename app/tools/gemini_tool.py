import openai
from typing import Dict, Any
from app.models.schemas import ToolResponse, ToolType
from app.models.settings import settings
import logging

logger = logging.getLogger(__name__)

class OpenAITool:
    def __init__(self):
        openai.api_key = settings.openai_api_key

    async def generate_content(self, prompt: str, system_prompt: str = "") -> ToolResponse:
        try:
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7
            )
            text = response.choices[0].message.content

            return ToolResponse(
                tool_type=ToolType.GEMINI,
                content={
                    "text": text,
                    "usage": response.usage if hasattr(response, "usage") else {}
                },
                success=True
            )
        except Exception as e:
            logger.error(f"OpenAI tool error: {str(e)}")
            return ToolResponse(
                tool_type=ToolType.GEMINI,
                content={},
                success=False,
                error_message=str(e)
            )