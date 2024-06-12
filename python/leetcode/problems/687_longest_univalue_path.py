# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def longestPathMatchingValue(node: TreeNode) -> int:
            paths = []
            if node.left and node.left.val == node.val:
                paths.append(
                    longestPathMatchingValue(node.left) + 1
                )
            if node.right and node.right.val == node.val:
                paths.append(
                    longestPathMatchingValue(node.right) + 1
                )
            return max(paths) if paths else 0

        paths = []
        if root and root.left and root.left.val == root.val:
            paths.append(
                longestPathMatchingValue(root.left) + 1
            )
        if root and root.right and root.right.val == root.val:
            paths.append(
                longestPathMatchingValue(root.right) + 1
            )
        answers = []
        answers.append(
            sum(paths)
        )
        if root and root.left:
            answers.append(
                self.longestUnivaluePath(root.left)
            )
        if root and root.right:
            answers.append(
                self.longestUnivaluePath(root.right)
            )
        
        return max(answers)

