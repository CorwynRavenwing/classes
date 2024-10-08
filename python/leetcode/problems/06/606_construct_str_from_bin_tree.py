# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        Val = root.val
        Left = self.tree2str(root.left)
        Right = self.tree2str(root.right)
        if Left or Right:
            Left = f'({Left})'
        if Right:
            Right = f'({Right})'
        return f'{Val}{Left}{Right}'

# NOTE: Accepted on first Submit
# NOTE: Runtime 35 ms Beats 96.55%
# NOTE: Memory 17.83 MB Beats 40.39%
