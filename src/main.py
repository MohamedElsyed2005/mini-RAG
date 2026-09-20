"""
main.py

Application entry point for the FastAPI application.

This module loads environment variables, creates the FastAPI application,
and registers the application routers.
"""

from fastapi import FastAPI
from routes import base, data

# Create the FastAPI application instance.
app = FastAPI()

# Register the base API router.
app.include_router(base.base_router)
app.include_router(data.data_router)