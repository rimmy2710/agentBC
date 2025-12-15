"""Entry point for the news-agent-poc smoke test."""

import sys

from .config import load_settings
from .openai_client import OpenAIResponsesClient


def main() -> None:
    """Load configuration, call the Responses API, and print the result."""

    try:
        settings = load_settings()
    except ValueError as exc:
        print(f"Configuration error: {exc}")
        sys.exit(1)

    client = OpenAIResponsesClient(settings)
    output_text = client.ping()
    print(output_text)


if __name__ == "__main__":
    main()
