# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        
        Pivot = max(nums)
        index = nums.index(Pivot)
        
        Left = self.constructMaximumBinaryTree(nums[:index])
        Right = self.constructMaximumBinaryTree(nums[index + 1:])

        return TreeNode(Pivot, Left, Right)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 132 ms Beats 69.80%
# NOTE: Memory 17.04 MB Beats 69.26%
