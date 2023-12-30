from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    nodes = dict()

    def __init__(self) -> None:
        self.nodes = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        if node.val in self.nodes:
            return self.nodes[node.val]
        
        newNode = Node(node.val)
        self.nodes[node.val] = newNode
        newNode.neighbors = [self.cloneGraph(v) for v in node.neighbors]
        return newNode