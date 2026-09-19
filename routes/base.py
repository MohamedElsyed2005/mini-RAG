"""
routes/base.py

Base API routes for the application.
This module defines the versioned API router and the welcome endpoint.
"""

import os
from fastapi import APIRouter

# Create the versioned API router.
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
def welcome():
    """Return the application name and version."""
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")

    return {
        "app_name": app_name,
        "app_version": app_version,
    }