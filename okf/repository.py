from .parser import parse_document
from .utils  import find_markdown_files

class OKFRepository:
    def __init__(self, root):
        self.root = root
        self.documents = {}

    def load(self):
        files = find_markdown_files(self.root)
        
        for file in files:
            document = parse_document(file)

            self.documents[document.title] = document