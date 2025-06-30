from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import UserPrompt, AgentResponse
from app.agents.router import route_prompt
from app.utils.logging import get_logger
from app.models.settings import settings
from fastapi.responses import JSONResponse  # Add this import

logger = get_logger(__name__)

app = FastAPI(
    title="Intelligent Agent API",
    description="API for routing prompts to intelligent agents with multiple tools",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process-prompt", response_model=AgentResponse)
async def process_prompt(prompt: UserPrompt):
    """
    Endpoint to process user prompts through the agent system.
    """
    try:
        logger.info(f"Processing prompt: {prompt.prompt_text}")
        response = await route_prompt(prompt)
        return response
    except Exception as e:
        logger.error(f"Error processing prompt: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health", response_class=JSONResponse, response_model=None)
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

# To run this file directly, ensure the parent directory is in sys.path
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)