import pytest
from unittest.mock import AsyncMock, patch
from app.agents.creative_agent import CreativeAgent
from app.models.schemas import UserPrompt, ToolType

@pytest.mark.asyncio
async def test_agent_weather_query():
    with patch('app.tools.weather_tool.WeatherTool.get_weather') as mock_weather:
        mock_weather.return_value = AsyncMock(
            success=True,
            content={"location": "London", "temperature": 15}
        )
        
        agent = CreativeAgent()
        response = await agent.process_prompt(UserPrompt(prompt_text="weather in London"))
        
        assert response.tool_used == ToolType.WEATHER
        assert "London" in response.response_text
        assert "15" in response.response_text

@pytest.mark.asyncio
async def test_agent_fallback():
    with patch('app.tools.gemini_tool.OpenAITool.generate_content') as mock_openai:
        mock_openai.return_value = AsyncMock(success=False)
        
        agent = CreativeAgent()
        response = await agent.process_prompt(UserPrompt(prompt_text="some prompt"))
        
        assert response.is_fallback