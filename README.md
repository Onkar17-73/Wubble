# Wubble
Intern Technical Assessment

## How to Run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**  
   - Copy `.env.example` to `.env` and fill in your API keys:
     - `OPENAI_API_KEY`
     - `WEATHER_API_KEY`

3. **Start the server**  
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**  
   - Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser for the interactive API docs.
