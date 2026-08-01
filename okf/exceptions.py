class OKFError(Exception):
    """
    Base exception for all OKF-related errors.
    """
    pass


class DocumentParseError(OKFError):
    """
    Raised when a markdown document cannot be parsed.
    """
    pass
