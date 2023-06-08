# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

COPY Procfile .
# Expose the port your FastAPI app will run on (change if necessary)
EXPOSE $PORT

# Define the command to run using the Procfile
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"