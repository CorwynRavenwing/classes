<pre># Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -&gt; int:

        # O(N) solution.  Improvement left as an exercise for the reader.
        
        if root is None:
            return 0
        else:
            return 1 + sum([
                self.countNodes(root.left),
                self.countNodes(root.right),
            ])

# NOTE: O(N) solution:
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 22.64%
# NOTE: Memory 23.26 MB Beats 82.29%

# NOTE: O(logN) solution:
# NOTE: 
# NOTE: 
# NOTE: 
# NOTE: </pre>