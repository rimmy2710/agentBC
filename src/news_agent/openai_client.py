"""Lightweight OpenAI Responses API wrapper."""

from openai import OpenAI

from .config import Settings


class OpenAIResponsesClient:
    """Client for issuing simple requests to the OpenAI Responses API."""

    def __init__(self, settings: Settings) -> None:
        self._client = OpenAI(api_key=settings.openai_api_key)

    def ping(self, message: str = "ping") -> str:
        """Send a basic prompt to verify connectivity."""

        response = self._client.responses.create(model="gpt-4.1-mini", input=message)
        output_text = getattr(response, "output_text", None)
        if output_text is None:
            raise RuntimeError("OpenAI response did not include output_text.")

        return output_text
