from typing import Any

import httpx

from .config import get_settings


class OllamaError(RuntimeError):
    """Raised when the local Ollama service cannot complete a request."""


SYSTEM_PROMPT = """You are EVI, a personal AI companion.

Your job is to help the user think clearly, understand their goals, plan realistically,
build useful habits, reflect on progress, and take practical next steps.

Be warm, clear, honest, and action-oriented.
Do not pretend to have performed actions you did not perform.
Do not make high-stakes medical, legal, or financial decisions for the user.
When an external action would affect the user's accounts, money, communications, or
important commitments, the future EVI action system must obtain appropriate permission.

Prefer practical guidance over generic motivation.
Ask a focused question when important context is missing.
"""


async def chat(message: str, history: list[dict[str, str]] | None = None) -> str:
    settings = get_settings()

    messages: list[dict[str, str]] = [{"role": "system", "content": SYSTEM_PROMPT}]

    if history:
        for item in history[-20:]:
            role = item.get("role")
            content = item.get("content")
            if role in {"user", "assistant"} and content:
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": message})

    payload: dict[str, Any] = {
        "model": settings.ollama_model,
        "messages": messages,
        "stream": False,
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{settings.ollama_base_url.rstrip('/')}/api/chat",
                json=payload,
            )
            response.raise_for_status()
    except httpx.HTTPError as exc:
        raise OllamaError(
            "EVI could not reach Ollama. Make sure Ollama is running and the configured model is available."
        ) from exc

    data = response.json()
    answer = data.get("message", {}).get("content")

    if not answer:
        raise OllamaError("Ollama returned an empty response.")

    return answer
