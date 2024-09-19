# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbersIncluding(self, partial: int, node: TreeNode) -> int:
        if not node:
            return 0
        partial *= 10
        partial += node.val
        if node.left or node.right:
            return sum([
                self.sumNumbersIncluding(partial, node.left),
                self.sumNumbersIncluding(partial, node.right),
            ])
        else:
            return partial

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return self.sumNumbersIncluding(0, root)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 34 ms Beats 68.21%
# NOTE: Memory 16.66 MB Beats 27.45%
