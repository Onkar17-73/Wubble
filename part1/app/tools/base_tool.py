from abc import ABC, abstractmethod
from typing import Dict, Any
from app.models.schemas import ToolResponse

class BaseTool(ABC):
    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> ToolResponse:
        pass