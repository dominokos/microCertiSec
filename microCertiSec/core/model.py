
from microCertiSec.core.edge import CEdge
from microCertiSec.core.node import CNode
from microCertiSec.core.edges import CEdges
from microCertiSec.core.nodes import CNodes


class CModel:

    def __init__(self, name: str, nodes: CNodes, edges: CEdges):
        self.name = name
        self.nodes = nodes
        self.edges = edges


    def __str__(self):
        return self.name
