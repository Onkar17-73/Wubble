import pytest
from app.models.schemas import UserPrompt, AgentResponse, ToolType
from pydantic import ValidationError

def test_user_prompt_validation():
    # Valid prompt
    prompt = UserPrompt(prompt_text="What's the weather?")
    assert prompt.prompt_text == "What's the weather?"
    
    # Empty prompt should raise error
    with pytest.raises(ValidationError):
        UserPrompt(prompt_text="")
    
    # Prompt with context
    prompt_with_context = UserPrompt(
        prompt_text="Tell me about Paris",
        context={"user_location": "London"}
    )
    assert prompt_with_context.context["user_location"] == "London"

def test_agent_response_validation():
    response = AgentResponse(
        response_text="It's sunny",
        tool_used=ToolType.WEATHER
    )
    assert response.response_text == "It's sunny"
    assert response.tool_used == ToolType.WEATHER
    assert not response.is_fallback
    
    # Missing required fields
    with pytest.raises(ValidationError):
        AgentResponse(response_text="Test")