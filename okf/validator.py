from .validation_models import (
    ValidationReport,
    ValidationIssue,
)


class RepositoryValidator:

    def __init__(self, repository):

        self.repository = repository

        self.report = ValidationReport()

    def validate(self):

        self.check_required_metadata()

        self.check_broken_links()

        return self.report

    def check_required_metadata(self):

        for document in self.repository.documents.values():

            if not document.title:

                self.report.issues.append(

                    ValidationIssue(

                        severity="ERROR",

                        issue_type="Missing Metadata",

                        message="Document has no title.",

                        document=document.path,
                    )
                )

            if not document.doc_type:

                self.report.issues.append(

                    ValidationIssue(

                        severity="ERROR",

                        issue_type="Missing Metadata",

                        message="Document has no type.",

                        document=document.path,
                    )
                )

    def check_broken_links(self):

        titles = self.repository.documents.keys() #Dictionary keys i.e. title names in our case


        for document in self.repository.documents.values():

            for link in document.links:

                if link not in titles:

                    self.report.issues.append(

                        ValidationIssue(

                            severity="WARNING",

                            issue_type="Broken Link",

                            message=f"'{link}' does not exist.",

                            document=document.path,
                        )
                    )

   # def check_duplicate_doc_titles(self):
        #Find duplicates in an array logic. Implemennt it later

    def check_orphan_docs(self):
        referenced = set()
        for document in repository.documents.values():
            referenced.update(document.links)

        for title in repository.documents:
            if title not in referenced:
                self.report.issues.append(

                        ValidationIssue(

                            severity="WARNING",

                            issue_type="Orphan Document",

                            message=f"'{title}' is not referenced anywhere.",

                            document=document.path,
                        )
                    )
    
    def print_summary(self):

        print("=" * 20)

        print("OKF Validation Report")

        print("=" * 20)

        print()

        print(f"Errors   : {len(self.errors)}")

        print(f"Warnings : {len(self.warnings)}")