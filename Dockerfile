# Use Python 3.11 base image
FROM python:3.11-slim

# Install Node.js and SQLite
RUN apt-get update && apt-get install -y \
    curl \
    sqlite3 \
    libsqlite3-dev \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy all files
COPY . .

# Install Python dependencies
RUN python -m venv .venv
ENV PATH="/app/.venv/bin:$PATH"
# Force rebuild - Railway cache issue fix
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list | grep psycopg2

# Build frontend
WORKDIR /app/frontend
RUN npm install
RUN npm run build

# Go back to app directory
WORKDIR /app

# Expose port
EXPOSE 8000

# Start the application
CMD cd backend && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
