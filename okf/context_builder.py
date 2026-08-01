class ContextBuilder:

    def __init__(self, repository):

        self.repository = repository

    def build(self, documents, max_documents=5):

        sections = []

        for document in documents[:max_documents]:

            document = result.document

            sections.append(
                f"""
            ========================================

            Title: {document.title}

            Summary:
            {document.summary}

            Content:
            {document.content}
            """
            )

        return "\n\n".join(sections)