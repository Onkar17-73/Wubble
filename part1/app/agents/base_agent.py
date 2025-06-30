from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from app.models.schemas import UserPrompt, AgentResponse, ToolType
from app.models.settings import settings

class BaseAgent(ABC):
    def __init__(self):
        self.system_prompt = settings.system_prompt
        self.fallback_response = settings.fallback_prompt

    @abstractmethod
    async def process_prompt(self, prompt: UserPrompt) -> AgentResponse:
        pass

    def create_response(
        self,
        response_text: str,
        tool_type: ToolType,
        metadata: Optional[Dict[str, Any]] = None,
        is_fallback: bool = False
    ) -> AgentResponse:
        return AgentResponse(
            response_text=response_text,
            tool_used=tool_type,
            metadata=metadata,
            is_fallback=is_fallback
        )