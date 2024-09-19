# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def addAsRightmost(self, root: TreeNode, branch: TreeNode) -> None:
        if not root:
            raise Exception(f'Empty root passed to addAsRightmost()')
        if root.right is None:
            root.right = branch
            return
        self.addAsRightmost(root.right, branch)
        return

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is not None:
            if root.right is not None:
                self.addAsRightmost(root.left, root.right)
                root.right = None
            root.right = root.left
            root.left = None
        if root.right is not None:
            self.flatten(root.right)
        return

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 37 ms Beats 67.50%
# NOTE: Memory 16.66 MB Beats 93.05%
