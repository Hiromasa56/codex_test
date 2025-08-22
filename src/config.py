"""Configuration utilities for accessing environment variables."""

from __future__ import annotations

import os

ENV_API_KEY = "GEMINI_API_KEY"


def get_api_key() -> str:
    """Return the Gemini API key from the environment.

    Raises:
        RuntimeError: If the API key is not set.
    """
    api_key = os.environ.get(ENV_API_KEY)
    if not api_key:
        raise RuntimeError(f"{ENV_API_KEY} is not set")
    return api_key
