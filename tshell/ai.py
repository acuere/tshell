import os
import logging

try:
    import openai
except ImportError:  # pragma: no cover - fallback if openai not installed
    openai = None

log = logging.getLogger(__name__)


def get_ai_response(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    """Get a response from the OpenAI API.

    This requires the `openai` package and an `OPENAI_API_KEY` environment variable.
    If the API key is missing or the package is unavailable, a placeholder response
    will be returned.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not openai or not api_key:
        log.debug("OpenAI not configured; returning placeholder response.")
        return "[AI] Response for: " + prompt

    openai.api_key = api_key
    try:
        chat_completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        return chat_completion.choices[0].message["content"].strip()
    except Exception as exc:  # pragma: no cover - network errors
        log.error("Error communicating with OpenAI: %s", exc)
        return "[AI] Error processing request"
