# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        V = root.val
        L = root.left.val if root.left else -1
        R = root.right.val if root.right else -1
        print(f"{V=} {L=} {R=}")
        if L == V:
            L = self.findSecondMinimumValue(root.left)
        if R == V:
            R = self.findSecondMinimumValue(root.right)
        if L == R:
            print(f"  -> {L=} {R=} | SAME")
            return R
        elif L == -1:
            print(f"  -> {L=} {R=} | RIGHT")
            return R
        elif R == -1:
            print(f"  -> {L=} {R=} | LEFT")
            return L
        else:
            M = min(L, R)
            print(f"  -> {L=} {R=} | MIN {M=}")
            return M

