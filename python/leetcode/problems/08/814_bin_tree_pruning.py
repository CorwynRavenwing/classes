# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # if we are a 1, or if we have subtrees, keep this node
        if root.val or root.left or root.right:
            return root
        # otherwise, prune
        return None

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 22 ms Beats 99.52%
# NOTE: Memory 16.54 MB Beats 43.65%
