# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if (not root1) and (not root2):
            # YES: both are empty
            return True
        
        if (not root1) or (not root2):
            # NO: only one is empty
            return False
        
        # count on neither being empty
        if root1.val != root2.val:
            # NO: values differ
            return False
        
        LL = self.flipEquiv(root1.left, root2.left)
        RR = self.flipEquiv(root1.right, root2.right)
        if LL and RR:
            # YES: this pair matches
            return True
        
        LR = self.flipEquiv(root1.left, root2.right)
        RL = self.flipEquiv(root1.right, root2.left)
        if LR and RL:
            # YES: this pair matches
            return True
        
        # NO: otherwise
        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.60 MB Beats 56.75%
