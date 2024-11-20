# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        Len = len(nums)
        Mid = Len // 2
        Left = nums[:Mid]
        Center = nums[Mid]
        Right = nums[Mid + 1:]
        LeftNode = self.sortedArrayToBST(Left)
        RightNode = self.sortedArrayToBST(Right)
        CenterNode = TreeNode(Center, LeftNode, RightNode)
        return CenterNode

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2 ms Beats 80.77%
# NOTE: Memory 17.91 MB Beats 24.40%
