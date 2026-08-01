from .ollama_client import OllamaClient
from .prompts import build_prompt


class Assistant:

    def __init__(self, repository):

        self.repository = repository
        self.llm = OllamaClient()

    def ask(self, question):

        context = self.repository.retrieve_context(question)

        prompt = build_prompt(
            context=context,
            question=question,
        )

        return self.llm.generate(prompt)