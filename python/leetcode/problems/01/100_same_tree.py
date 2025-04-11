<pre># Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -&gt; bool:

        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return all([
            p.val == q.val,
            self.isSameTree(p.left, q.left),
            self.isSameTree(p.right, q.right),
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.72 MB Beats 66.20%</pre>