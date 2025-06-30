# Stage 1: Build (optimized caching)
FROM python:3.9-slim as builder

WORKDIR /app
COPY ../part1/requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime (minimal image)
FROM python:3.9-slim
WORKDIR /app

# Copy only necessary artifacts
COPY --from=builder /root/.local /root/.local
COPY ../part1/app ./app

# Configure production environment
ENV PATH=/root/.local/bin:$PATH \
    PYTHONPATH=/app \
    PORT=8000 \
    WORKERS=4 \
    TIMEOUT=60 \
    MAX_REQUESTS=1000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:$PORT/health || exit 1

EXPOSE $PORT
CMD ["sh", "-c", \
    "uvicorn app.main:app --host 0.0.0.0 --port $PORT \
    --workers $WORKERS --timeout-keep-alive $TIMEOUT \
    --max-requests $MAX_REQUESTS"]