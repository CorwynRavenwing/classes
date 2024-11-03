# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # we borrow some code from #105:

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

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)  # b/c this is a BST
        return self.buildTree(preorder, inorder)

# NOTE: re-used entire prior version, with some glue code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: O(N * Log(N))
# NOTE: Memory 16.70 MB Beats 9.91%
# NOTE: O(N)
