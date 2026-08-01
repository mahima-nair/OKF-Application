from pathlib import Path

def find_markdown_files(root):

    return sorted(Path(root).rglob("*.md"))