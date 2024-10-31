# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        parentOf = {}
        siblingOf = {}
        depthOf = {}

        parentOf[0] = 0
        siblingOf[0] = 0
        depthOf[0] = 0

        # @cache    # cache doesn't help, this is only called once per node
        # returns maximum depth; sets parentOf and depthOfOtherBranch values
        def prepare(node: TreeNode) -> int:

            if not node:
                raise ValueError(f'We should not have been passed a null {node=}')
            
            VAL = lambda N: (N.val if N else 0)

            N = VAL(node)
            L = VAL(node.left)
            R = VAL(node.right)

            # print(f'prepare({N}): {L=} {R=}')

            if L:
                parentOf[L] = N
                siblingOf[L] = R
                depthOf[L] = prepare(node.left)

            if R:
                parentOf[R] = N
                siblingOf[R] = L
                depthOf[R] = prepare(node.right)
            
            return 1 + max(depthOf[L], depthOf[R])
        
        rootVal = root.val
        depthOf[rootVal] = prepare(root)

        # print(f'{parentOf=}')
        # print(f'{siblingOf=}')
        # print(f'{depthOf=}')

        def depth_if_node_had_value(N: int, V: int) -> int:

            while N in siblingOf:
                original = depthOf[N]
                sibling = siblingOf[N]
                siblingDepth = depthOf[sibling]
                depth = max(V, siblingDepth)
                parent = parentOf[N]
                if original == depth:
                    print(f'original == depth')
                    return depthOf[rootVal]

                N = parent
                V = depth + 1

            return V

        def depth_without_node(N: int) -> int:
            return depth_if_node_had_value(N, 0)

        def doQuery(Q: int) -> int:
            return depth_without_node(Q) - 1
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 42.0% (HARD)
# NOTE: Time Limit Exceeded for large inputs
