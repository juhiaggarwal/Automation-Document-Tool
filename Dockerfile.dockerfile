FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wkhtmltopdf \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (optional, default is 8000)
EXPOSE 8000

# Start the app
CMD ["gunicorn", "app:app"]
