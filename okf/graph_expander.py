class GraphExpander:

    def __init__(self, repository):

        self.repository = repository

    def expand(self, search_results):

        expanded = []

        seen = set()

        for result in search_results:

            document = result.document

            # Include the original document
            if document.title not in seen:

                expanded.append(document)

                seen.add(document.title)

            # Include neighboring documents
            for neighbor in self.repository.graph.neighbor_documents(document.title):

                if neighbor.title not in seen:

                    expanded.append(neighbor)

                    seen.add(neighbor.title)

        return expanded