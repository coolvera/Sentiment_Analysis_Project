FROM python:3.13-slim

WORKDIR /app

# Copy everything from app/ into container's /app directory
COPY app/ .

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]
