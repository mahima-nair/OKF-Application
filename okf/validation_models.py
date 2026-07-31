from dataclasses import dataclass, field


@dataclass
class ValidationIssue:
    """
    Represents one validation problem.
    """

    severity: str      # ERROR or WARNING

    issue_type: str    # Broken Link, Duplicate Title, etc.

    message: str

    document: str = ""


@dataclass
class ValidationReport:

    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def errors(self):

        return [
            issue
            for issue in self.issues
            if issue.severity == "ERROR"
        ]

    @property
    def warnings(self):

        return [
            issue
            for issue in self.issues
            if issue.severity == "WARNING"
        ]