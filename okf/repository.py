from .parser import parse_document
from .utils  import find_markdown_files
from .validator import RepositoryValidator
from .graph import KnowledgeGraph
from .query_engine import QueryEngine
from .context_builder import ContextBuilder
from .graph_expander import GraphExpander


class OKFRepository:
    def __init__(self, root):
        self.root = root
        self.documents = {}
        self.graph = KnowledgeGraph()
        self.query_engine = QueryEngine(self)
        self.context_builder = ContextBuilder(self)
        self.graph_expander = GraphExpander(self)

    def load(self):

        files = find_markdown_files(self.root)

        for file in files:

            document = parse_document(file)

            # Check duplicate titles
            if document.title in self.documents:
                raise ValueError(
                    f"Duplicate document title: {document.title}"
                )

            self.documents[document.title] = document

        # Build the knowledge graph
        self.graph.build(self.documents)
    
        # Validate the repository
        self.validate()

        #Print the repo
        print(repo.graph.graph.nodes())
        print(repo.graph.graph.edges())

    def validate(self):
        validator = RepositoryValidator(self)
        self.validation_report = validator.validate()
        return self.validation_report

    def search(self, query):
        return self.query_engine.search(query)
 
    def expand(self, results):

        return self.graph_expander.expand(results)

    def build_context(self, documents):

        return self.context_builder.build(documents)

    def retrieve_context(self, query):

        results = self.search(query)

        expanded = self.expand(results)

        context = self.build_context(expanded)

        return context


