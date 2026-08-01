from openai import OpenAI

from .config import LLMConfig


class LLMClient:

    def __init__(self):

        provider = LLMConfig.PROVIDER.lower()

        if provider == "ollama":

            self.client = OpenAI(
                base_url=LLMConfig.OLLAMA_BASE_URL,
                api_key="ollama",
            )

            self.model = LLMConfig.OLLAMA_MODEL

        elif provider == "openai":

            self.client = OpenAI(
                api_key=LLMConfig.OPENAI_API_KEY,
            )

            self.model = LLMConfig.OPENAI_MODEL

        else:

            raise ValueError(
                f"Unsupported provider: {provider}"
            )

    def generate(self, prompt):

        response = self.client.chat.completions.create(

        model=self.model,

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content