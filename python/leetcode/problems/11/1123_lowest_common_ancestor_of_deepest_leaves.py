# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # @cache
        def maxDepth(node: TreeNode) -> int:
            if not node:
                return -1
            else:
                return max([
                    maxDepth(node.left),
                    maxDepth(node.right),
                ]) + 1
        
        Left = maxDepth(root.left)
        Right = maxDepth(root.right)

        if Left > Right:
            return self.lcaDeepestLeaves(root.left)
        if Left < Right:
            return self.lcaDeepestLeaves(root.right)
        if Left == Right:
            return root
        
        raise Exception(f'Error comparing {Left=} <=> {Right=}')

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Without cache:
# NOTE: Runtime 10 ms Beats 8.79%
# NOTE: Memory 17.02 MB Beats 30.19%
# NOTE: With cache:
# NOTE: Runtime 24 ms Beats 8.24%
# NOTE: Memory 18.63 MB Beats 11.00%
# NOTE: Time actually 2.5 times SLOWER, memory slightly worse
