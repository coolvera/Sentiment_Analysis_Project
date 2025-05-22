# Use an official Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app/app.py"]
