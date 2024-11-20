# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        def flattenTree(node: TreeNode) -> List[int]:
            print(f'flattenTree([{node.val if node is not None else None}]):')
            if node is None:
                return []
            return flattenTree(node.left) + [node.val] + flattenTree(node.right)
        
        arr = flattenTree(root)
        print(f'{arr=}')
        return [[-999]]

        def findMin(Q: int, node: TreeNode, bestSoFar=None, depth=0) -> int:
            while True:
                # margin = '  ' * depth
                # print(f'{margin}findMin({Q},[{node.val if node is not None else None}],{bestSoFar}):')
                if node is None:
                    if bestSoFar is None:
                        # print(f'{margin}  not found')
                        return -1
                    else:
                        # print(f'{margin}  return bestSoFar')
                        return bestSoFar
                elif node.val == Q:
                    # print(f'{margin}  found exact')
                    return node.val
                elif node.val < Q:
                    if bestSoFar is None or bestSoFar < node.val:
                        bestSoFar = node.val
                        # print(f'{margin}  new largest value {bestSoFar}')
                    node = node.right
                    depth += 1
                elif node.val > Q:
                    node = node.left
                    depth += 1
                else:
                    raise Exception("should not get here")

        def findMax(Q: int, node: TreeNode, bestSoFar=None, depth=0) -> int:
            while True:
                # margin = '  ' * depth
                # print(f'{margin}findMax({Q},[{node.val if node is not None else None}],{bestSoFar}):')
                if node is None:
                    if bestSoFar is None:
                        # print(f'{margin}  not found')
                        return -1
                    else:
                        # print(f'{margin}  return bestSoFar')
                        return bestSoFar
                elif node.val == Q:
                    # print(f'{margin}  found exact')
                    return node.val
                elif node.val < Q:
                    node = node.right
                    depth += 1
                elif node.val > Q:
                    if bestSoFar is None or bestSoFar > node.val:
                        bestSoFar = node.val
                        # print(f'{margin}  new smallest value {bestSoFar}')
                    node = node.left
                    depth += 1
                else:
                    raise Exception("should not get here")

        def doQuery(Q: int) -> Tuple[int,int]:
            return (
                findMin(Q, root),
                findMax(Q, root),
            )
        
        return [
            doQuery(Q)
            for Q in queries
        ]
# NOTE: this version *also* times out with large inputs.
#   I tried flattening the nodes into an array: this *ALSO* times out.
#   I have no idea what to try next.
