from dataclasses import dataclass


@dataclass
class SearchResult:

    document: object

    score: float