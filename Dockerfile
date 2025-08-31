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
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -r requirements.txt

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
