from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.models.schemas import UserPrompt, AgentResponse
from app.agents.router import route_prompt
from app.models.settings import settings
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Agent API",
    description="API for processing prompts with OpenAI",
    version="1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom validation error handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc}")
    # Print the error details for debugging
    print("VALIDATION ERROR DETAILS:", exc.errors())
    print("REQUEST BODY:", exc.body)
    return JSONResponse(
        status_code=422,
        content={
            "detail": exc.errors(),
            "body": exc.body,
            "custom_message": "Validation failed: Please ensure your prompt is not empty, not just whitespace, and under 1000 characters."
        },
    )

@app.post("/process-prompt", response_model=AgentResponse)
async def process_prompt(prompt: UserPrompt):
    try:
        logger.info(f"Processing prompt from user {prompt.user_id}")
        return await route_prompt(prompt)
    except Exception as e:
        logger.error(f"Server error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "error": str(e),
                "solution": "Please try again with a different prompt"
            }
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0"}