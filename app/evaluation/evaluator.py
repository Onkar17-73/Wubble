from typing import List, Dict, Any
from app.models.schemas import AgentResponse
from app.evaluation.judge import LLMJudge
from app.evaluation.test_cases import TEST_CASES
import logging

logger = logging.getLogger(__name__)

class Evaluator:
    def __init__(self):
        self.judge = LLMJudge()
        self.test_cases = TEST_CASES

    async def evaluate_agent(self, agent_func) -> Dict[str, Any]:
        results = []
        
        for case in self.test_cases:
            try:
                response = await agent_func(case["prompt"])
                evaluation = await self.judge.evaluate_response(
                    case["prompt"],
                    response,
                    case.get("expected_tool"),
                    case.get("expected_characteristics")
                )
                
                results.append({
                    "test_case": case["name"],
                    "passed": evaluation["passed"],
                    "feedback": evaluation["feedback"],
                    "response": response.dict()
                })
            except Exception as e:
                logger.error(f"Error evaluating test case {case['name']}: {str(e)}")
                results.append({
                    "test_case": case["name"],
                    "passed": False,
                    "feedback": f"Evaluation failed: {str(e)}",
                    "response": None
                })
        
        summary = {
            "total_tests": len(results),
            "passed": sum(1 for r in results if r["passed"]),
            "failed": sum(1 for r in results if not r["passed"])
        }
        
        return {
            "summary": summary,
            "details": results
        }