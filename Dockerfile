FROM node:18-slim

# Install Python and system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./
COPY pyproject.toml uv.lock ./

# Install Node.js dependencies
RUN npm install

# Install Python dependencies
RUN pip3 install gradio requests

# Copy all source files
COPY . .

# Build the application
RUN npm run build

# Create SQLite database directory
RUN mkdir -p data

# Expose port
EXPOSE 7860

# Set environment variables
ENV NODE_ENV=production
ENV PORT=7860
ENV DATABASE_URL=sqlite:./data/safeguard.db

# Start command
CMD ["python3", "app.py"]