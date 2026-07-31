import re

import frontmatter

from .models import OKFDocument


WIKI_LINK = re.compile(r"\[\[(.*?)\]\]")


def parse_document(path):

    post = frontmatter.load(path) # frontmatter is used to read the YAML data which contains the metadata of the markdown file

    metadata = post.metadata

    content = post.content

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