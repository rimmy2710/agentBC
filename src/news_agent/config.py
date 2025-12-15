"""Configuration loader for the news-agent-poc project."""

from dataclasses import dataclass
import os
from dotenv import load_dotenv


@dataclass
class Settings:
    """Application settings loaded from environment variables."""

    openai_api_key: str


def load_settings() -> Settings:
    """Load and validate required environment variables."""

    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required. Set it in your environment or .env file.")

    return Settings(openai_api_key=api_key)
