<pre># Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -&gt; int:
        
        if root is None:
            return 0
        
        return 1 + max([
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 45.19%
# NOTE: Memory 19.10 MB Beats 47.85%</pre>