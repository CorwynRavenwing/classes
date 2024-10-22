# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        levelSums = {}
        def setLevelSum(node: TreeNode, level=0) -> None:
            if node is None:
                return
            levelSums.setdefault(level, 0)
            levelSums[level] += node.val
            setLevelSum(node.left, level + 1)
            setLevelSum(node.right, level + 1)
            return

        setLevelSum(root)
        print(f'{levelSums=}')

        Sums = tuple(sorted(levelSums.values(), reverse=True))
        print(f'{Sums=}')
        
        if len(Sums) < k:
            return -1

        return Sums[k - 1]  # -1 b/c zero-based array
# NOTE: Runtime 317 ms Beats 28.08%
# NOTE: Memory 57.49 MB Beats 10.73%
# NOTE: re-ran later for the challenge and received:
# NOTE: Runtime 113 ms Beats 96.87%
# NOTE: Memory 64.48 MB Beats 5.33%
