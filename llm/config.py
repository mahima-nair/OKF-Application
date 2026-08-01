# To read all the env variables and store its values
from dotenv import load_dotenv
import os

load_dotenv()


class LLMConfig:

    PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL")

    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")