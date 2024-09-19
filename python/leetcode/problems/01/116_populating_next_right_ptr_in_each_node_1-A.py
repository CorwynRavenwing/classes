"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def nextLayer(self, nodes: 'List[Optional[Node]]') -> 'List[Optional[Node]]':
        return [
            N
            for node in nodes
            if node
            for N in (node.left, node.right)
            if N
        ]

    def connectGroup(self, nodes: 'List[Optional[Node]]'):
        for (A, B) in pairwise(nodes):
            A.next = B
        return

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        nodes = [root]
        while nodes:
            self.connectGroup(nodes)
            nodes = self.nextLayer(nodes)
        return root

# NOTE: works, but with O(N) space requirements.  We want O(1).
