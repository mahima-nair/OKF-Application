def build_prompt(context, question):

    return f"""
You are an AI assistant answering questions from an internal knowledge base.

Answer only using the provided context.

If the answer is not contained in the context, say that you don't know.

-------------------------

Context

{context}

-------------------------

Question

{question}

Answer:
"""