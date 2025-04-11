<pre># Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # we borrow some code from #104:
    @cache
    def maxDepth(self, root: Optional[TreeNode]) -&gt; int:

        print(f'  MD({root.val if root else &quot;-&quot;})')
        
        if root is None:
            return 0
        
        return 1 + max([
            self.maxDepth(root.left),
            self.maxDepth(root.right),
        ])

    def isBalanced(self, root: Optional[TreeNode]) -&gt; bool:
        print(f'IB({root.val if root else &quot;-&quot;})')

        if root is None:
            return True
        
        Left = self.maxDepth(root.left)
        Right = self.maxDepth(root.right)
        if abs(Right - Left) &gt; 1:
            return False
        
        return all([
            self.isBalanced(root.left),
            self.isBalanced(root.right),
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with unbalanced subtree)

# NOTE: without cache:
# NOTE: Runtime 79 ms Beats 5.90%
# NOTE: Memory 18.97 MB Beats 25.66%

# NOTE: with cache:
# NOTE: Runtime 28 ms Beats 5.90%
# NOTE: Memory 24.33 MB Beats 6.96%

# NOTE: much worse memory, much faster, identical runtime percentage</pre>