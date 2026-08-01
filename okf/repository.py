from .parser import parse_document
from .utils  import find_markdown_files
from .validator import RepositoryValidator
from .graph import KnowledgeGraph

class OKFRepository:
    def __init__(self, root):
        self.root = root
        self.documents = {}
        self.graph = KnowledgeGraph()

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
