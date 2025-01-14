# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install Git and other dependencies
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install MLflow
RUN pip install mlflow

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME MLflow-Demo

# Run the training script and then start MLflow UI
CMD ["sh", "-c", "python train.py && mlflow ui --host 0.0.0.0 --port 5000"]
