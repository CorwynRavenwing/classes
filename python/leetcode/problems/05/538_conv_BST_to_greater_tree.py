# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        sum_so_far = 0

        def convertPartialBST(node: TreeNode) -> TreeNode:
            nonlocal sum_so_far
            if not node:
                return None
            # Yes, these are being done RIGHT, CENTER, LEFT:
            Right = convertPartialBST(node.right)
            sum_so_far += node.val  # add value of this node, to the global total
            Val = sum_so_far        # store the value after Right and before Left
            Left = convertPartialBST(node.left)
            return TreeNode(Val, Left, Right)
        
        return convertPartialBST(root)

# NOTE: Accepted on second Run (first was 1-char typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 75 ms Beats 5.13%
# NOTE: Memory 20.25 MB Beats 5.13%
