# Wubble
Intern Technical Assessment

Wubble is a production-ready FastAPI service that routes user prompts to an intelligent agent, which utilizes multiple tools (OpenAI and Weather API) to generate structured, safe, and helpful responses. The project is fully containerized for easy deployment and includes an automated evaluation framework.

---

## How to Run (Locally)

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

---

## How to Run (Docker - part2)

1. **Set your API keys as environment variables** (recommended for production):
   - On Windows (Command Prompt):
     ```
     set OPENAI_API_KEY=your_openai_key
     set WEATHER_API_KEY=your_weather_key
     ```
   - On PowerShell:
     ```
     $env:OPENAI_API_KEY="your_openai_key"
     $env:WEATHER_API_KEY="your_weather_key"
     ```
   - On macOS/Linux:
     ```
     export OPENAI_API_KEY=your_openai_key
     export WEATHER_API_KEY=your_weather_key
     ```

2. **Build and run the Docker image:**
   ```bash
   cd part2
   ./run.sh
   ```
   > On Windows, use `./run.sh` in PowerShell or Git Bash.

   Or manually:
   ```bash
   docker build -t ai-agent .
   docker run -d -p 8000:8000 \
     -e OPENAI_API_KEY="your_openai_key" \
     -e WEATHER_API_KEY="your_weather_key" \
     --memory="1g" --cpus="1.0" \
     --name ai-agent \
     ai-agent
   ```

3. **Access the API:**
   - Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health: [http://localhost:8000/health](http://localhost:8000/health)

---

## System Prompt & Agent Behavior

- The agent is guided by a system prompt enforcing a helpful, safe, and concise tone.
- Fallback logic ensures a safe response if tools fail or the prompt is off-topic.
- The agent uses at least two tools:
  - **OpenAI** (for general queries)
  - **Weather API** (for weather-related queries)
  - Additional custom logic for general/fallback responses.

---

## Automated Evaluation Framework

- The project includes an automated evaluation framework to validate:
  - Input validation and error handling
  - Correct routing to tools based on prompt type
  - Adherence to system prompt (tone, safety, fallback)
  - Pass/fail results for 5–8 test cases (typical, edge, off-topic)

---

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

---

## Project Structure

- `app/` — FastAPI app and agent logic
- `tests/` — Unit and evaluation tests
- `.env.example` — Example environment variables
- `part1/` — Source code and local setup
- `part2/` — Dockerfile, deployment scripts, and containerization instructions

---

## Notes

- Ensure API keys are set for all integrations.
- For Docker deployment, see the `part2` folder.
- See `tests/test_evaluation.py` for evaluation framework and test cases.
- The Docker image is production-ready and can be deployed to any Docker-compatible platform.

---

## Demo Video

Below is a demo video showing the project in action (local run):

[View Demo Video on Google Drive](https://drive.google.com/file/d/1KXnPiFE60fYrREljZnx8J3WXd0eE-pE6/view?usp=sharing)
<!-- Replace YOUR_DRIVE_LINK_HERE with your actual Google Drive share link. -->
