# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            # print(f"{None}")
            return 0
        
        # print(f"{root.val=} L=? R=?")
        L = self.minDepth(root.left)
        # print(f"{root.val=} {L=} R=?")
        R = self.minDepth(root.right)
        # print(f"{root.val=} {L=} {R=}")
        children = list([
            val
            for val in [L, R]
            if val != 0
        ])
        # print(f"{children}")
        if not children:
            children = [0]
        return 1 + min(children)

