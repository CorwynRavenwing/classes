# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        # @cache
        def prepare(node: TreeNode) -> Dict[int,int]:

            VAL = lambda N: (N.val if N else '-')

            # print(f'prepare({VAL(node)}):')

            if not node:
                answer = {0: 0}
                # print(f'prepare({VAL(node)}): {answer}')
                return answer

            # print(f'prepare({VAL(node)}): L={VAL(node.left)} R={VAL(node.right)}')

            Left = prepare(node.left)
            Right = prepare(node.right)

            # print(f'prepare({VAL(node)}): {Left=} {Right=}')

            answer = {node.val: 0}
            for val, depth in Left.items():
                if val == 0:
                    continue
                answer[val] = 1 + max(depth, Right[0])
            for val, depth in Right.items():
                if val == 0:
                    continue
                answer[val] = 1 + max(depth, Left[0])
            answer[0] = 1 + max(Left[0], Right[0])
            # print(f'prepare({VAL(node)}): {answer}')
            return answer
        
        depth_without = prepare(root)

        def doQuery(Q: int) -> int:
            return depth_without[Q] - 1
        
        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 42.0% (HARD)
# NOTE: Time Limit Exceeded for large inputs
