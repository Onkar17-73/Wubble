import openai
from typing import Dict, Any, Optional, List  
from app.models.schemas import AgentResponse, ToolType
from app.models.settings import settings
import logging

logger = logging.getLogger(__name__)

class LLMJudge:
    def __init__(self):
        openai.api_key = settings.openai_api_key
    
    async def evaluate_response(
        self,
        user_prompt: str,
        agent_response: AgentResponse,
        expected_tool: Optional[ToolType] = None,
        expected_characteristics: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        evaluation_prompt = self._create_evaluation_prompt(
            user_prompt,
            agent_response,
            expected_tool,
            expected_characteristics
        )
        
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[{"role": "system", "content": evaluation_prompt}],
                temperature=0
            )
            
            feedback = response.choices[0].message.content
            passed = "PASS" in feedback.upper()
            
            return {
                "passed": passed,
                "feedback": feedback
            }
        except Exception as e:
            logger.error(f"Error in LLM judge: {str(e)}")
            return {
                "passed": False,
                "feedback": f"Evaluation failed: {str(e)}"
            }

    def _create_evaluation_prompt(
        self,
        user_prompt: str,
        agent_response: AgentResponse,
        expected_tool: Optional[ToolType],
        expected_characteristics: Optional[List[str]]
    ) -> str:
        prompt = f"""
        You are an AI response evaluator. Carefully analyze the following:
        
        USER PROMPT: {user_prompt}
        AGENT RESPONSE: {agent_response.response_text}
        TOOL USED: {agent_response.tool_used}
        IS FALLBACK: {agent_response.is_fallback}
        
        Evaluation Criteria:
        1. Was the appropriate tool used? {"Expected: " + expected_tool.value if expected_tool else "No specific tool expected"}
        2. Does the response match the expected characteristics? {expected_characteristics if expected_characteristics else "N/A"}
        3. Is the response helpful, accurate, and appropriate?
        4. For off-topic/inappropriate prompts, did the agent respond correctly?
        
        Provide detailed feedback and conclude with either PASS or FAIL in all caps.
        """
        
        return prompt