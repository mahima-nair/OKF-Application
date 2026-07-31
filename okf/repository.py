from .parser import parse_document
from .utils  import find_markdown_files
from .validator import RepositoryValidator

class OKFRepository:
    def __init__(self, root):
        self.root = root
        self.documents = {}

    def load(self):
        files = find_markdown_files(self.root)
        
        for file in files:
            document = parse_document(file)

        # If we find any document having duplicate titles, raise the error
        if document.title in self.documents:

            raise ValueError(

                f"Duplicate document title: {document.title}"
            )

            self.documents[document.title] = document

    def validate(self):
        validator = RepositoryValidator(self)
        self.validation_report = validator.validate()
        return self.validation_report
