# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def parentValueOf(targetValue: int, node: TreeNode, parentValue: int) -> int:
            label = (node.val if node else None)
            print(f'parentValueOf({targetValue},{label},{parentValue})')
            if node is None:
                return None
            if node.val == targetValue:
                return parentValue
            attempt = parentValueOf(targetValue, node.left, node.val)
            if attempt is not None:
                return attempt
            attempt = parentValueOf(targetValue, node.right, node.val)
            if attempt is not None:
                return attempt
            return None

        def levelOf(targetValue: int, node: TreeNode, level=0) -> int:
            label = (node.val if node else None)
            print(f'levelOf({targetValue},{label},{level})')
            if node is None:
                return None
            if node.val == targetValue:
                return level
            attempt = levelOf(targetValue, node.left, level+1)
            if attempt is not None:
                return attempt
            attempt = levelOf(targetValue, node.right, level+1)
            if attempt is not None:
                return attempt
            return None
        
        return (
            (
                levelOf(x, root) == levelOf(y, root)
            ) and (
                parentValueOf(x, root, 0) != parentValueOf(y, root, 0)
            )
        )
# NOTE: Runtime 41 ms Beats 23.86%
# NOTE: Memory 16.81 MB Beats 16.10%
