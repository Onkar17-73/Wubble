# Wubble
Intern Technical Assessment

## How to Run

1. **Create and activate a virtual environment**  
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**  
   - Copy `.env.example` to `.env` and fill in your API keys:
     - `OPENAI_API_KEY`
     - `WEATHER_API_KEY`

4. **Start the server**  
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API**  
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser for the interactive API docs.

## System Prompt & Agent Behavior

- The agent is guided by a system prompt enforcing a helpful, safe, and concise tone.
- Fallback logic ensures a safe response if tools fail or the prompt is off-topic.
- The agent uses at least two tools:
  - **OpenAI** (for general queries)
  - **Weather API** (for weather-related queries)
  - Additional custom logic for general/fallback responses.

## Automated Evaluation Framework

- The project includes an automated evaluation framework to validate:
  - Input validation and error handling
  - Correct routing to tools based on prompt type
  - Adherence to system prompt (tone, safety, fallback)
  - Pass/fail results for 5–8 test cases (typical, edge, off-topic)

## Running Tests

1. **Run all tests (including evaluation):**
   ```bash
   pytest
   ```

2. **Test coverage includes:**
   - Pydantic model validation
   - Tool routing logic
   - System prompt effects
   - Automated evaluation of agent responses

## Project Structure

- `app/` — FastAPI app and agent logic
- `tests/` — Unit and evaluation tests
- `.env.example` — Example environment variables

## Notes

- Ensure API keys are set for all integrations.
- See `tests/test_evaluation.py` for evaluation framework and test cases.
