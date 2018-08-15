# Use an official Python runtime as a parent image
FROM python:3-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container in its /app/
# directory
ADD main.py requirements.txt /app/

# Install Python requirements
RUN pip install -r requirements.txt

# Logs can be collected here
RUN mkdir /logs

# Results can be collected here
RUN mkdir /results
