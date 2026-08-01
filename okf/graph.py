#networkx: library to build a graph for connecting all the knowledge md components together

import networkx as nx 

class KnowledgeGraph:

    def __init__(self):

        #Networkx provides 2 types of graphs: Undirectional (Graph) and Directional (DiGraph)
        self.graph = nx.DiGraph()

    # Add the document as a node in the graph
    def add_document(self, document):

        self.graph.add_node(
            document.title,
            document=document, #So later we can retrieve the full document directly from the graph.
        )

    #Adding the edges (links between document nodes)
    def add_links(self, document):

        for link in document.links:

            self.graph.add_edge(
                document.title,
                link,
            )

    #Building the graph
    def build(self, documents):

        # Building the nodes
        for document in documents.values():

            self.add_document(document)

        #Connecting the nodes
        for document in documents.values():

            self.add_links(document)


#Querying the graph (adding neighbours)
    def neighbors(self, title):

        return list(
            self.graph.successors(title)
        )

 # Finding the neighbouring docs
     def neighbor_documents(self, title):

        docs = []

        for neighbor in self.graph.successors(title):

            docs.append(

                self.graph.nodes[neighbor]["document"]

            )

        return docs
