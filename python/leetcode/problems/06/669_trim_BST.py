# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if low <= root.val <= high:
            # I'm okay, check my children
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        
        # otherwise, this node itself is being trimmed;
        # but bear in mind that all of root.left will be less than node.val,
        # and all of root.right will be more than node.val, so if we are
        # out of bounds then so is one or the other of our children

        if root.val < low:
            # root.left is also < low
            return self.trimBST(root.right, low, high)
        
        if root.val > high:
            # right.right is also > high
            return self.trimBST(root.left, low, high)
        
        raise Exception(f'logic error: it should be impossible to get here.  {low=} {root.val=} {high=}')
        return None

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 49 ms Beats 28.78%
# NOTE: Memory 19.55 MB Beats 19.47%
