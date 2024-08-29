
class CNode:
    """Class CNode for nodes in the model / DFD.
    A node is represented by its name, stereotypes and tagged_values.
    """

    def __init__(self, name, stereotypes, traceability, connected_nodes = set(), tagged_values = {}):
        self.name = name
        self.stereotypes = stereotypes
        self.traceability = traceability
        self.connected_nodes = connected_nodes
        self.tagged_values = tagged_values

    def __str__(self):
        return f"Node {self.name}; stereotypes {self.stereotypes}"
