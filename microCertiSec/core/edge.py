from microCertiSec.core.node import CNode


class CEdge:
    """Class CEdge for edges in the model / DFD.
    Each edge is represented by its sender and receiver, stereotypes, and tagged values.
    """

    def __init__(self, sender: CNode, receiver: CNode, stereotypes: list, traceability, tagged_values = {}):
        self.sender = sender
        self.receiver = receiver
        self.stereotypes = stereotypes
        self.traceability = traceability
        self.name = sender.name + " -> " + receiver.name
        self.tagged_values = tagged_values

    def __str__(self):
        return f"Edge {self.name}; stereotypes {self.stereotypes}"
