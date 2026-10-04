# llm_client.py
import requests

DEFAULT_MODEL = "llama3.1:8b"
OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_text(prompt: str, model: str = DEFAULT_MODEL, temperature: float = 0.3) -> str:
    """
    Generate text using a local Ollama model.
    Returns the full response text.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
        },
    }
    resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    return data.get("response", "")