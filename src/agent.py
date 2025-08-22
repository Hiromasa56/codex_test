"""Simple entry point demonstrating API key usage."""

from __future__ import annotations

from .config import get_api_key


def create_client() -> dict:
    """Create a mock client using the Gemini API key.

    In a real implementation, this would initialize the Google Gemini client.
    """
    api_key = get_api_key()
    return {"api_key": api_key}


def main() -> None:
    client = create_client()
    # To avoid leaking the full key, show only partial information
    print(f"Client initialized with key prefix: {client['api_key'][:4]}***")


if __name__ == "__main__":
    main()
