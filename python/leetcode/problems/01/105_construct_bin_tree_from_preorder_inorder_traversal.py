# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # print(f'buildTree({preorder},{inorder})')
        if preorder == inorder == []:
            return None
        center = preorder[0]
        if preorder == inorder == [center]:
            return TreeNode(center)
        index = inorder.index(center)
        print(f'  {center=} {index=}')
        leftPre = preorder[1:index + 1]
        leftIn = inorder[0:index]
        # print(f'  {leftPre=} {leftIn=}')
        rightPre = preorder[index + 1:]
        rightIn = inorder[index + 1:]
        # print(f'  {rightPre=} {rightIn=}')
        Left = self.buildTree(leftPre, leftIn)
        Right = self.buildTree(rightPre, rightIn)
        return TreeNode(center, Left, Right)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 139 ms Beats 29.18%
# NOTE: Memory 88.45 MB Beats 9.41%
