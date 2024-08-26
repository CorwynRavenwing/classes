"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []
        return (
            [
                Answer
                for Child in root.children
                for Answer in self.postorder(Child)
            ] + [
                root.val
            ]
        )

