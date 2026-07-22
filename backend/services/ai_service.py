"""
CivicIQ -- AI Service
Thin wrapper around Groq LLM for narrative text generation.
Falls back to deterministic mock output if no API key is available.
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Primary and fallback models
PRIMARY_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"

_client = None


def get_client():
    """Get or create the Groq client. Returns None if no API key."""
    global _client
    if _client is not None:
        return _client
    if not GROQ_API_KEY or GROQ_API_KEY == "your_api_key_here":
        return None
    try:
        from groq import Groq
        _client = Groq(api_key=GROQ_API_KEY)
        return _client
    except Exception as e:
        print(f"[AI_SERVICE] Failed to initialize Groq client: {e}")
        return None


async def generate_narrative(
    system_prompt: str,
    user_prompt: str,
    fallback_text: str = "",
    max_tokens: int = 500,
    temperature: float = 0.3,
) -> str:
    """
    Generate narrative text using Groq LLM.
    If no API key or call fails, returns fallback_text.

    Uses llama-3.3-70b-versatile as primary model.
    Falls back to llama-3.1-8b-instant if primary model is unavailable.
    """
    client = get_client()
    if client is None:
        return fallback_text

    for model in [PRIMARY_MODEL, FALLBACK_MODEL]:
        try:
            response = client.chat.completions.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            error_msg = str(e).lower()
            # If it's a model-specific error, try the fallback model
            if model == PRIMARY_MODEL and ("model" in error_msg or "not found" in error_msg or "unavailable" in error_msg):
                print(f"[AI_SERVICE] Primary model {PRIMARY_MODEL} unavailable, trying fallback: {e}")
                continue
            # For other errors (rate limit, timeout, auth), don't retry with different model
            print(f"[AI_SERVICE] LLM call failed ({model}): {e}. Using fallback text.")
            return fallback_text

    # Both models failed
    print(f"[AI_SERVICE] All models failed. Using fallback text.")
    return fallback_text
