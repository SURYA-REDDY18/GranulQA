from typing import Dict, List, Set


class Node:
    """
    Represents a node in the hierarchical tree structure.
    """

    def __init__(self, text: str, index: int, children: Set[int], embeddings) -> None:
        self.text = text
        self.index = index
        self.children = children
        self.embeddings = embeddings


# In raptor/tree_structures.py

class Tree:
    """
    Represents the entire hierarchical tree structure.
    """
    def __init__(
        self, all_nodes, root_nodes, leaf_nodes, num_layers, layer_to_nodes
    ) -> None:
        self.all_nodes     = all_nodes
        self.root_nodes    = root_nodes
        self.leaf_nodes    = leaf_nodes
        self.num_layers    = num_layers
        self.layer_to_nodes= layer_to_nodes

    def get_summary(self, node_id: int) -> str:
        """
        Return the summary for the given node_id (if set),
        otherwise fall back to the node's full text.
        """
        node = self.all_nodes[node_id]
        return getattr(node, "summary", node.text)
