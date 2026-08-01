import re

import frontmatter

from .models import OKFDocument
from .exceptions import DocumentParseError

WIKI_LINK = re.compile(r"\[\[(.*?)\]\]")


def parse_document(path):
    """
    Parse a single OKF markdown document.
    """

    try:

        # Read markdown + YAML frontmatter
        post = frontmatter.load(path)

        metadata = post.metadata

        content = post.content

        # Find all [[Wiki Links]]
        links = WIKI_LINK.findall(content)

        return OKFDocument(

            title=metadata["title"],

            doc_type=metadata["type"],

            version=metadata.get("version", ""),

            author=metadata.get("author", ""),

            last_updated=metadata.get("last_updated", ""),

            tags=metadata.get("tags", []),

            summary=metadata.get("summary", ""),

            content=content,

            path=str(path),

            links=links,
        )

    except KeyError as e:

        raise DocumentParseError(
            f"{path}: Missing required metadata field {e}"
        )

    except Exception as e:

        raise DocumentParseError(
            f"{path}: {e}"
        )