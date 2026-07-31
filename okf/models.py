from dataclasses import dataclass, field

@dataclass
class OKFDocument:
    """
    Represents one Knowledge document"
    """
    title : str

    doc_type: str

    version : str = ""

    author : str = ""

    last_updated : str = ""

    tags : list[str] = field(default_factory=list)

    summary: str = ""

    content : str = ""

    path : str = ""
    
    links : list[str] = field(default_factory=list)
