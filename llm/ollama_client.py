from ollama import Client


class OllamaClient:

    def __init__(
        self,
        host="http://localhost:11434",
        model="llama3.2",
    ):
        self.client = Client(host=host)
        self.model = model

    def generate(self, prompt):

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]