from .search_models import SearchResult


class QueryEngine:

    def __init__(self, repository):

        self.repository = repository

    def search(self, query):

        query = query.lower()

        results = []

        for document in self.repository.documents.values():

            score = 0

            if query in document.title.lower():

                score += 10

            if query in document.summary.lower():

                score += 5

            if query in document.content.lower():

                score += 2

            if score > 0:

                results.append(

                    SearchResult(

                        document=document,

                        score=score,
                    )
                )

        results.sort(

            key=lambda result: result.score,

            reverse=True,
        )

        return results