# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # we borrow some code from #108:

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

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inOrder(node: TreeNode) -> List[int]:
            if not node:
                return ()
            else:
                L = inOrder(node.left)
                R = inOrder(node.right)
                C = (node.val,)
                return L + C + R
                
        in_order = inOrder(root)
        print(f'{in_order=}')

        return self.sortedArrayToBST(in_order)

# NOTE: re-used the prior version's code unchanged, plus some glue
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 52 ms Beats 10.85%
# NOTE: Memory 22.56 MB Beats 24.49%

# NOTE: Acceptance Rate 84.8% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 39 ms Beats 31.50%
# NOTE: Memory 24.92 MB Beats 34.32%
