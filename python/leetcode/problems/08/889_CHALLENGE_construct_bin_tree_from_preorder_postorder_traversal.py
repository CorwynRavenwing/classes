# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            assert not postorder
            return None
        
        thisValue = preorder.pop(0)
        assert thisValue == postorder.pop(-1)
        print(f'construct({thisValue})')

        if not preorder:
            assert not postorder
            return TreeNode(thisValue)
        
        leftVal = preorder[0]
        leftIndex = postorder.index(leftVal) + 1
        print(f'  split@{leftVal} left=[:{leftIndex}] right=[{leftIndex}:]')
        print(f'    L: {preorder[:leftIndex]},{postorder[:leftIndex]}')
        Left = self.constructFromPrePost(
            preorder[:leftIndex],
            postorder[:leftIndex],
        )
        print(f'    R: {preorder[leftIndex:]},{postorder[leftIndex:]}')
        Right = self.constructFromPrePost(
            preorder[leftIndex:],
            postorder[leftIndex:],
        )
        print(f'    {Left=} {Right=}')
        return TreeNode(thisValue, Left, Right)

# NOTE: Runtime 57 ms Beats 12.41%
# NOTE: Memory 16.84 MB Beats 13.59%

# NOTE: re-ran for challenge:
# NOTE: Runtime 59 ms Beats 9.15%
# NOTE: Memory 17.91 MB Beats 28.31%
