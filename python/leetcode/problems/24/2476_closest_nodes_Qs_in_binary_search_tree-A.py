# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        def findMin(Q: int, node: TreeNode, bestSoFar=None, depth=0) -> int:
            # margin = '  ' * depth
            # print(f'{margin}findMin({Q},[{node.val if node is not None else None}],{bestSoFar}):')
            if node is None:
                if bestSoFar is None:
                    # print(f'{margin}  not found')
                    return -1
                else:
                    # print(f'{margin}  return bestSoFar')
                    return bestSoFar
            if node.val == Q:
                # print(f'{margin}  found exact')
                return node.val
            if node.val < Q:
                if bestSoFar is None or bestSoFar < node.val:
                    bestSoFar = node.val
                    # print(f'{margin}  new largest value {bestSoFar}')
                return findMin(Q, node.right, bestSoFar, depth+1)
            if node.val > Q:
                return findMin(Q, node.left, bestSoFar, depth+1)

        def findMax(Q: int, node: TreeNode, bestSoFar=None, depth=0) -> int:
            # margin = '  ' * depth
            # print(f'{margin}findMax({Q},[{node.val if node is not None else None}],{bestSoFar}):')
            if node is None:
                if bestSoFar is None:
                    # print(f'{margin}  not found')
                    return -1
                else:
                    # print(f'{margin}  return bestSoFar')
                    return bestSoFar
            if node.val == Q:
                # print(f'{margin}  found exact')
                return node.val
            if node.val < Q:
                return findMax(Q, node.right, bestSoFar, depth+1)
            if node.val > Q:
                if bestSoFar is None or bestSoFar > node.val:
                    bestSoFar = node.val
                    # print(f'{margin}  new smallest value {bestSoFar}')
                return findMax(Q, node.left, bestSoFar, depth+1)

        def doQuery(Q: int) -> Tuple[int,int]:
            return (
                findMin(Q, root),
                findMax(Q, root),
            )
        
        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: the normal way of doing this, which times out for large inputs
