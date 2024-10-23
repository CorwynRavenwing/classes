# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        
        answer = []

        def flip(node: TreeNode):
            nonlocal answer
            V = node.val
            answer.append(V)
            print(f'  flip({V})')
            (node.left, node.right) = (node.right, node.left)
            return
        
        def checkVoyage(node: TreeNode):
            nonlocal answer
            if not node:
                return

            if node.val != voyage[0]:
                answer = [-1]
                return
            del voyage[0]

            if (not node.left) and (not node.right):
                return
            
            if node.left and node.right:
                if node.right.val == voyage[0]:
                    flip(node)
            
            checkVoyage(node.left)
            checkVoyage(node.right)
        
        checkVoyage(root)
        if -1 in answer:
            return [-1]
        else:
            return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 97.73%
# NOTE: Memory 16.86 MB Beats 7.27%
