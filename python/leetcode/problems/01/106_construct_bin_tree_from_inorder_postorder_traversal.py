# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # we borrow some code from #105:

        # print(f'buildTree({inorder},{postorder})')
        if inorder == postorder == []:
            return None
        center = postorder[-1]
        if inorder == postorder == [center]:
            return TreeNode(center)
        index = inorder.index(center)
        print(f'  {center=} {index=}')
        leftIn = inorder[0:index]
        leftPost = postorder[0:index]
        # print(f'  {leftIn=} {leftPost=}')
        rightIn = inorder[index + 1:]
        rightPost = postorder[index:-1]
        # print(f'  {rightIn=} {rightPost=}')
        Left = self.buildTree(leftIn, leftPost)
        Right = self.buildTree(rightIn, rightPost)
        return TreeNode(center, Left, Right)

# NOTE: Reused all code from previous version; reversed polarity
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 198 ms Beats 5.24%
# NOTE: Memory 88.62 MB Beats 8.96%
