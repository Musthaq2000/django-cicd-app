# ---------- STAGE 1: BUILD ----------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies (only for build stage)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements first (for caching)
COPY requirements.txt .

# Create virtual environment
RUN python -m venv /opt/venv

# Activate venv and install dependencies
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


# ---------- STAGE 2: RUNTIME ----------
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Add venv to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copy project code
COPY . .

# Create directory for DB volume
RUN mkdir -p /data

EXPOSE 8000

CMD ["sh", "-c", "cd project && python manage.py migrate && gunicorn project.wsgi:application --bind 0.0.0.0:8000"]
