from typing import Optional, Dict, Any
from app.agents.base_agent import BaseAgent
from app.models.schemas import UserPrompt, AgentResponse, ToolType
from app.tools.gemini_tool import OpenAITool
from app.tools.weather_tool import WeatherTool
from app.models.settings import settings
import logging

logger = logging.getLogger(__name__)

class CreativeAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.gemini_tool = OpenAITool()
        self.weather_tool = WeatherTool()
        self.system_prompt = settings.system_prompt

    async def process_prompt(self, prompt: UserPrompt) -> AgentResponse:
        try:
            # Check if prompt is about weather
            if self._is_weather_query(prompt.prompt_text):
                weather_data = await self.weather_tool.get_weather(prompt.prompt_text)
                if weather_data.success:
                    response_text = self._format_weather_response(weather_data.content)
                    return self.create_response(
                        response_text=response_text,
                        tool_type=ToolType.WEATHER,
                        metadata=weather_data.content
                    )
            
            # Default to Gemini for creative tasks
            gemini_response = await self.gemini_tool.generate_content(
                prompt.prompt_text,
                system_prompt=self.system_prompt
            )
            
            if gemini_response.success:
                return self.create_response(
                    response_text=gemini_response.content["text"],
                    tool_type=ToolType.GEMINI,
                    metadata=gemini_response.content
                )
            
            # Fallback if all tools fail
            return self.create_response(
                response_text=self.fallback_response,
                tool_type=ToolType.GENERAL,
                is_fallback=True
            )
            
        except Exception as e:
            logger.error(f"Error processing prompt: {str(e)}")
            return self.create_response(
                response_text=self.fallback_response,
                tool_type=ToolType.GENERAL,
                is_fallback=True
            )

    def _is_weather_query(self, text: str) -> bool:
        weather_keywords = ["weather", "temperature", "forecast", "rain", "sunny", "humidity"]
        return any(keyword in text.lower() for keyword in weather_keywords)

    def _format_weather_response(self, weather_data: Dict[str, Any]) -> str:
        location = weather_data.get("location", "the requested location")
        temp = weather_data.get("temperature", "unknown")
        condition = weather_data.get("condition", "unknown conditions")
        return f"The current weather in {location} is {temp}°C with {condition}."