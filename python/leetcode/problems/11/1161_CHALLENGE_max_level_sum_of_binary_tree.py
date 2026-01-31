# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        sumByLevel = {}
        def setSumByLevel(node: TreeNode, level=0) -> None:
            if node is None:
                return
            sumByLevel.setdefault(level, 0)
            sumByLevel[level] += node.val
            setSumByLevel(node.left, level+1)
            setSumByLevel(node.right, level+1)
            return
        setSumByLevel(root, 1)  # for some reason top level is "1" here
        print(f'{sumByLevel=}')

        maxLevelSum = max(sumByLevel.values())
        print(f'{maxLevelSum=}')

        levelsWithMaxSum = [
            level
            for level, total in sumByLevel.items()
            if total == maxLevelSum
        ]
        print(f'{levelsWithMaxSum=}')

        return min(levelsWithMaxSum)

# NOTE: Acceptance Rate 69.9% (medium)

# NOTE: Runtime 182 ms Beats 11.35%
# NOTE: Memory 20.12 MB Beats 5.05%
