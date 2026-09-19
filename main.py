"""
main.py

Application entry point for the FastAPI application.

This module loads environment variables, creates the FastAPI application,
and registers the application routers.
"""

from fastapi import FastAPI
from dotenv import load_dotenv

from routes import base

# Load environment variables from the .env file.
load_dotenv()

# Create the FastAPI application instance.
app = FastAPI()

# Register the base API router.
app.include_router(base.base_router)