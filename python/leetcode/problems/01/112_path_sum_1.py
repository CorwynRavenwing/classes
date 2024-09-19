# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # print(f'HPS({root},{targetSum})')

        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            # leaf node
            return (targetSum == 0)
        # elif targetSum <= 0:
        #     return False
        
        return any([
            self.hasPathSum(root.left, targetSum),
            self.hasPathSum(root.right, targetSum),
        ])

# NOTE: Runtime 39 ms Beats 71.18%
# NOTE: Memory 17.45 MB Beats 48.87%
