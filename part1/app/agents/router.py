from app.models.schemas import UserPrompt, AgentResponse
from app.agents.creative_agent import CreativeAgent
from app.utils.logging import get_logger
from fastapi import HTTPException

logger = get_logger(__name__)

async def route_prompt(prompt: UserPrompt) -> AgentResponse:
    try:
        # Additional validation can be added here
        if not prompt.prompt_text.strip():
            raise HTTPException(
                status_code=422,
                detail={"error": "Prompt cannot be empty"}
            )
            
        agent = CreativeAgent()
        return await agent.process_prompt(prompt)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Routing error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={"error": "Internal processing error"}
        )