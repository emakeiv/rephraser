#!/bin/bash

# Activate the virtual environment
# pipenv shell

# Start the FastAPI application using Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload