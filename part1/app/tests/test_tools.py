import pytest
from unittest.mock import AsyncMock, patch
from app.tools.weather_tool import WeatherTool
from Wubble.app.tools.openai_tool import OpenAITool
from app.models.schemas import ToolResponse

@pytest.mark.asyncio
async def test_weather_tool_success():
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_response = AsyncMock()
        mock_response.json.return_value = {
            "location": {"name": "London"},
            "current": {"temp_c": 15, "condition": {"text": "Cloudy"}}
        }
        mock_get.return_value = mock_response
        
        tool = WeatherTool()
        result = await tool.get_weather("weather in London")
        
        assert result.success
        assert result.content["location"] == "London"
        assert result.content["temperature"] == 15

@pytest.mark.asyncio
async def test_openai_tool_failure():
    with patch('openai.ChatCompletion.acreate') as mock_openai:
        mock_openai.side_effect = Exception("API error")
        
        tool = OpenAITool()
        result = await tool.generate_content("test prompt")
        
        assert not result.success
        assert "API error" in result.error_message