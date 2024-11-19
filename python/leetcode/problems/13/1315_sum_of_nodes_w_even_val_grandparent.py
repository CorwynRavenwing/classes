# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def sumMatchingNodes(node: TreeNode, parentEven: bool, grandparentEven: bool) -> int:
            print(f'SMN({node.val if node else None},{parentEven},{grandparentEven})')
            if not node:
                return 0
            thisNodeEven = (node.val % 2 == 0)
            return sum([
                node.val if grandparentEven else 0,
                sumMatchingNodes(node.left, thisNodeEven, parentEven),
                sumMatchingNodes(node.right, thisNodeEven, parentEven),
            ])
        
        return sumMatchingNodes(root, False, False)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 73 ms Beats 5.29%
# NOTE: Memory 19.92 MB Beats 7.12%
