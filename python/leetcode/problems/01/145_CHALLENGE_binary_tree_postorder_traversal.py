# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        return (
            (
                self.postorderTraversal(root.left)
            ) + (
                self.postorderTraversal(root.right)
            ) + (
                [root.val]
            )
        )
# NOTE: Runtime 35 ms Beats 55.78%
# NOTE: Memory 16.49 MB Beats 64.22%
