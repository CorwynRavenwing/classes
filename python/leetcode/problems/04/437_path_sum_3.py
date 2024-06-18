# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def checkFromHere(node: TreeNode, target: int) -> int:
            answer = 0
            new_target = target - node.val
            if new_target == 0:
                answer += 1
            if node.left:
                answer += checkFromHere(node.left, new_target)
            if node.right:
                answer += checkFromHere(node.right, new_target)
            return answer

        def checkAllNodes(node: TreeNode) -> int:
            nonlocal targetSum
            answer = 0
            if node:
                answer += checkFromHere(node, targetSum)
                if node.left:
                    answer += checkAllNodes(node.left)
                if node.right:
                    answer += checkAllNodes(node.right)
            return answer
        
        return checkAllNodes(root)

