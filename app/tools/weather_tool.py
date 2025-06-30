import httpx
from typing import Dict, Any
from app.models.schemas import ToolResponse, ToolType
from app.models.settings import settings
import logging
import re

logger = logging.getLogger(__name__)

class WeatherTool:
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    async def get_weather(self, query: str) -> ToolResponse:
        try:
            location = self._extract_location(query)
            if not location:
                return ToolResponse(
                    tool_type=ToolType.WEATHER,
                    content={},
                    success=False,
                    error_message="No location found in query"
                )

            async with httpx.AsyncClient() as client:
                params = {
                    "key": settings.weather_api_key,
                    "q": location,
                    "aqi": "no"
                }
                response = await client.get(self.BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()

            return ToolResponse(
                tool_type=ToolType.WEATHER,
                content={
                    "location": data["location"]["name"],
                    "temperature": data["current"]["temp_c"],
                    "condition": data["current"]["condition"]["text"],
                    "wind_kph": data["current"]["wind_kph"],
                    "humidity": data["current"]["humidity"]
                },
                success=True
            )
        except Exception as e:
            logger.error(f"Weather tool error: {str(e)}")
            return ToolResponse(
                tool_type=ToolType.WEATHER,
                content={},
                success=False,
                error_message=str(e)
            )

    def _extract_location(self, text: str) -> str:
        # Simple location extraction - in a real app this would be more sophisticated
        patterns = [
            r"weather in ([\w\s]+)",
            r"temperature in ([\w\s]+)",
            r"how is the weather in ([\w\s]+)",
            r"what's the weather like in ([\w\s]+)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # Fallback to the last word that's not a weather term
        weather_terms = {"weather", "temperature", "forecast", "rain", "sunny"}
        words = [word for word in text.split() if word.lower() not in weather_terms]
        return words[-1] if words else ""