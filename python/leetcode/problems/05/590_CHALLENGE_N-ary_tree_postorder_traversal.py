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
# NOTE: Accepted on first Submit
# NOTE: Runtime 35 ms Beats 97.81%
# NOTE: Memory 18.26 MB Beats 43.75%
