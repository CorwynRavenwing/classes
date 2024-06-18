# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def maxRob(root: Optional[TreeNode]) -> Tuple[int,int]:
            # returns (rob, skip)
            # rob: amount if we rob the root node,
            # skip: amount if we do not
            if not root:
                return (0, 0)
            (LeftRob, LeftSkip) = maxRob(root.right)
            (RightRob, RightSkip) = maxRob(root.left)

            robRoot = sum([
                root.val,
                LeftSkip,
                RightSkip,
            ])
            skipRoot = sum([
                0,
                max(LeftRob, LeftSkip),
                max(RightRob, RightSkip),
            ])
            return (robRoot, skipRoot)

        return max(maxRob(root))

