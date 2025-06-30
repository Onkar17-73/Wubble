# Wubble - Docker Deployment

## How to Use the Docker Image

1. **Set your API keys as environment variables** (recommended):
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
   ```sh
   cd part2
   ./run.sh
   ```
   > On Windows, use `./run.sh` in PowerShell or Git Bash.

   Or manually:
   ```sh
   docker build -t ai-agent .
   docker run -d -p 8000:8000 ^
     -e OPENAI_API_KEY="your_openai_key" ^
     -e WEATHER_API_KEY="your_weather_key" ^
     --memory="1g" --cpus="1.0" ^
     --name ai-agent ^
     ai-agent
   ```

3. **Access the API:**
   - Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health: [http://localhost:8000/health](http://localhost:8000/health)

## Notes

- Adjust memory/CPU in `run.sh` or the `docker run` command as needed.
- The image is production-ready and can be deployed to any Docker-compatible platform.