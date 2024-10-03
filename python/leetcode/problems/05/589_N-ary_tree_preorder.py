"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:

    # we borrow some code from #290:

    def preorder(self, root: 'Node') -> List[int]:

        if root is None:
            return []
        return (
            [
                root.val
            ] + [
                Answer
                for Child in root.children
                for Answer in self.preorder(Child)
            ]
        )

# NOTE: re-used entire prior version, with minor changes
# NOTE: Accepted on first Run
# NOTE: Accepted on first Run
# NOTE: Runtime 58 ms Beats 7.48%
# NOTE: Memory 18.59 MB Beats 7.48%
