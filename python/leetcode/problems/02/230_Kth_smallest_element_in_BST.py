# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        return (
            (
                self.inorderTraversal(root.left)
            ) + (
                [root.val]
            ) + (
                self.inorderTraversal(root.right)
            )
        )

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        array = self.inorderTraversal(root)

        return array[k - 1]     # one-based question, zero-based array

# NOTE: Accepted on second Run (first was simple typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 51 ms Beats 19.16%
# NOTE: Memory 19.66 MB Beats 5.87%
