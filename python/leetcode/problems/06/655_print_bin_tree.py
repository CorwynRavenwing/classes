# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def TreeHeight(node: TreeNode) -> int:
            if node is None:
                return 0
            return max([
                1 + TreeHeight(node.left),
                1 + TreeHeight(node.right),
            ])
        
        height = TreeHeight(root) - 1
        M = height + 1
        N = 2 ** (height + 1) - 1
        print(f'Tree {height=} {M=} {N=}')
        matrix = [
            [''] * N
            for _ in range(M)
        ]

        def showMatrix(label: str):
            nonlocal matrix
            print(f'===== {label} =====')
            for row in matrix:
                formatted = [
                    '.' if val == '' else val
                    for val in row
                ]
                print(f''.join(formatted))
            return

        def placeNodesInMatrix(R: int, C: int, node: TreeNode):
            nonlocal height
            nonlocal matrix
            if node is None:
                return
            showMatrix(f'top {node.val} @{(R,C)}')
            matrix[R][C] = str(node.val)
            offset = 2 ** (height - R - 1)
            placeNodesInMatrix(
                R + 1,
                C - offset,
                node.left
            )
            placeNodesInMatrix(
                R + 1,
                C + offset,
                node.right
            )
            showMatrix(f'end {node.val} @{(R,C)}')
            return

        showMatrix('blank')
        R = 0
        C = (N - 1) // 2
        print(f'Top of tree: {(R,C)=}')

        placeNodesInMatrix(R, C, root)

        return matrix

# NOTE: Accepted on first Submit
# NOTE: Runtime 37 ms Beats 60.99%
# NOTE: Memory 16.78 MB Beats 6.03%
