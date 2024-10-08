# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        # we borrow some code from #538:
        
        sum_so_far = 0

        def convertPartialBST(node: TreeNode) -> TreeNode:
            nonlocal sum_so_far
            if not node:
                return None
            # Yes, these are being done RIGHT, CENTER, LEFT:
            Right = convertPartialBST(node.right)
            sum_so_far += node.val  # add value of this node, to the global total
            Val = sum_so_far        # store the value after Right and before Left
            Left = convertPartialBST(node.left)
            return TreeNode(Val, Left, Right)
        
        return convertPartialBST(root)

# NOTE: re-used precise code of prior version: it works perfectly
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 38 ms Beats 36.81%
# NOTE: Memory 16.66 MB Beats 10.10%
