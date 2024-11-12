# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def sizeOfSubtree(node: TreeNode) -> int:
            if not node:
                return 0
            return sum([
                sizeOfSubtree(node.left),
                sizeOfSubtree(node.right),
            ]) + 1
        
        def findNodeWithValue(node: TreeNode, value: int) -> TreeNode:
            if not node:
                return None
            if node.val == value:
                return node
            Left = findNodeWithValue(node.left, value)
            Right = findNodeWithValue(node.right, value)

            return (Left if Left else Right)
        
        player_one_node = findNodeWithValue(root, x)

        TreeSize = sizeOfSubtree(root)
        X_Size = sizeOfSubtree(player_one_node)
        LeftSize = sizeOfSubtree(player_one_node.left)
        RightSize = sizeOfSubtree(player_one_node.right)
        print(f'{TreeSize=} {X_Size=}')
        ParentSize = TreeSize - X_Size
        assert X_Size == 1 + LeftSize + RightSize
        print(f'{ParentSize=} {LeftSize=} {RightSize=}')
        Y_Size = max(ParentSize, LeftSize, RightSize)

        return ((Y_Size * 2) > TreeSize)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 1 ms Beats 20.43%
# NOTE: Memory 16.66 MB Beats 50.88%
