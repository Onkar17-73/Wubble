from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from enum import Enum

class ToolType(str, Enum):
    OPENAI = "openai"
    WEATHER = "weather"
    GENERAL = "general"

class UserPrompt(BaseModel):
    prompt_text: str = Field(..., min_length=1)
    user_id: Optional[str] = None
    context: Optional[Dict[str, Any]] = None

class AgentResponse(BaseModel):
    response_text: str
    tool_used: ToolType
    metadata: Optional[Dict[str, Any]] = None
    is_fallback: bool = False

class ToolResponse(BaseModel):
    tool_type: ToolType
    content: Dict[str, Any]
    success: bool
    error_message: Optional[str] = None