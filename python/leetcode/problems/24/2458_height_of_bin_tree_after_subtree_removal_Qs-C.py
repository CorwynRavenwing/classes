# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def depthWithout(node: TreeNode, skipValue: int) -> int:
            if not node:
                return 0
            if node.val == skipValue:
                return 0
            return 1 + max([
                depthWithout(node.left, skipValue),
                depthWithout(node.right, skipValue),
            ])

        def depth_without_node(N: int) -> int:
            return depthWithout(root, N)

        def doQuery(Q: int) -> int:
            return depth_without_node(Q) - 1
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 42.0% (HARD)
# NOTE: Time Limit Exceeded for large inputs
