"""
routes/base.py

Base API routes for the application.
This module defines the versioned API router and the welcome endpoint.
"""

import os
from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

# Create the versioned API router.
base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    """Return the application name and version."""
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name": app_name,
        "app_version": app_version,
    }