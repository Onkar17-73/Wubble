from app.models.schemas import UserPrompt, AgentResponse
from app.agents.creative_agent import CreativeAgent
from app.utils.logging import get_logger

logger = get_logger(__name__)

async def route_prompt(prompt: UserPrompt) -> AgentResponse:
    """
    Routes the prompt to the appropriate agent.
    Currently we only have one agent, but this provides flexibility for future expansion.
    """
    try:
        agent = CreativeAgent()
        return await agent.process_prompt(prompt)
    except Exception as e:
        logger.error(f"Error routing prompt: {str(e)}")
        raise