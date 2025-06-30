from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from enum import Enum

class ToolType(str, Enum):
    GEMINI = "openai"  # Change value to "openai" for clarity
    WEATHER = "weather"
    GENERAL = "general"

class UserPrompt(BaseModel):
    prompt_text: str = Field(..., min_length=1, max_length=1000, description="The user's input prompt")
    user_id: Optional[str] = Field(None, description="Optional user identifier for personalization")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context for the prompt")

    @validator('prompt_text')
    def validate_prompt_text(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Prompt text cannot be empty")
        return v

class ToolResponse(BaseModel):
    tool_type: ToolType
    content: Dict[str, Any]
    success: bool
    error_message: Optional[str] = None

class AgentResponse(BaseModel):
    response_text: str
    tool_used: ToolType
    metadata: Optional[Dict[str, Any]] = None
    is_fallback: bool = False