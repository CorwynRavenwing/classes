# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @cache
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        # @cache
        def longestZigZagIncremental(node: TreeNode, lengthSoFar: int, directionLeft: bool) -> int:
            print(f'LZZI({node.val if node else None},{lengthSoFar},{"L" if directionLeft else "R"})')
            if not node:
                return lengthSoFar - 1
            
            if directionLeft:
                return max([
                    longestZigZagIncremental(node.left, 1, True),
                    longestZigZagIncremental(node.right, lengthSoFar + 1, False),
                ])
            else:
                return max([
                    longestZigZagIncremental(node.left, lengthSoFar + 1, True),
                    longestZigZagIncremental(node.right, 1, False),
                ])
        
        return max([
            longestZigZagIncremental(root, 0, True),
            longestZigZagIncremental(root, 0, False),
        ])

# NOTE: Accepted on first Submit
# NOTE: Runtime 555 ms Beats 5.05%
# NOTE: Memory 32.07 MB Beats 21.76%
