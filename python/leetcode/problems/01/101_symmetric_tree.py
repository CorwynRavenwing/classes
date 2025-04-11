<pre># Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -&gt; bool:
        
        def areMirrors(A: TreeNode, B: TreeNode) -&gt; bool:

            if A is None and B is None:
                return True
            
            if A is None or B is None:
                return False
            
            return all([
                A.val == B.val,
                areMirrors(A.left, B.right),
                areMirrors(A.right, B.left),
            ])

        return areMirrors(root.left, root.right)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 18.02 MB Beats 12.95%</pre>