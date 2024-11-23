# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def GN(node: TreeNode, maxValue: int) -> int:
            if not node:
                return 0
            myself = (
                1
                if (maxValue <= node.val)
                else 0
            )
            maxValue = max(node.val, maxValue)
            return sum([
                GN(node.left, maxValue),
                GN(node.right, maxValue),
                myself,
            ])
        
        NEGATIVE_INFINITY = float('-inf')
        return GN(root, NEGATIVE_INFINITY)

# NOTE: Accepted on second Run (first was GT/LT error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 147 ms Beats 20.27%
# NOTE: Memory 31.14 MB Beats 65.27%
