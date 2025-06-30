from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, Any
from enum import Enum

class ToolType(str, Enum):
    OPENAI = "openai"
    WEATHER = "weather"
    GENERAL = "general"

class ToolResponse(BaseModel):
    tool_type: ToolType
    content: Dict[str, Any]
    success: bool
    error_message: Optional[str] = None

class UserPrompt(BaseModel):
    prompt_text: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        example="What's the weather in London?",
        description="User's query for the AI agent"
    )
    user_id: Optional[str] = Field(
        None,
        example="user_123",
        description="Optional user identifier"
    )
    context: Optional[Dict[str, Any]] = Field(
        None,
        example={"location": "London"},
        description="Additional context for the query"
    )

    @validator('prompt_text')
    def validate_prompt_text(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Prompt text cannot be empty or whitespace. Please enter a valid prompt.")
        if len(v) > 1000:
            raise ValueError("Prompt text too long (max 1000 characters).")
        return v

class AgentResponse(BaseModel):
    response_text: str = Field(..., example="The capital of France is Paris")
    tool_used: ToolType = Field(..., example="openai")
    metadata: Optional[Dict[str, Any]] = Field(
        None,
        example={"usage": {"prompt_tokens": 10, "completion_tokens": 5}}
    )
    is_fallback: bool = Field(False, example=False)