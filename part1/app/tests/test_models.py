import pytest
from app.models.schemas import UserPrompt, AgentResponse
from pydantic import ValidationError

def test_valid_prompt():
    valid_prompt = UserPrompt(
        prompt_text="Valid question?",
        user_id="user_123",
        context={"location": "London"}
    )
    assert valid_prompt.prompt_text == "Valid question?"

@pytest.mark.parametrize("prompt_text", [
    "",
    "   ",
    None,
    "x" * 1001  # 1001 characters
])
def test_invalid_prompts(prompt_text):
    with pytest.raises(ValidationError):
        UserPrompt(prompt_text=prompt_text)

def test_response_validation():
    valid_response = AgentResponse(
        response_text="Valid response",
        tool_used="openai"
    )
    assert valid_response.tool_used == "openai"