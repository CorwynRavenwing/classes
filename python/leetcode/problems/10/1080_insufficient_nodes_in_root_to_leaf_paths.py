# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        VAL = lambda X: (X.val if X else "-")
        # print(f'sSub({VAL(root)},{limit})')

        @cache
        def maxSumToLeaf(node: TreeNode) -> int:
            # print(f'max({VAL(node)})')
            if not node:
                # print(f'  -> None')
                return None
            answers = [
                maxSumToLeaf(node.left),
                maxSumToLeaf(node.right),
            ]
            # print(f'max({VAL(node)}): {answers}')
            while None in answers:
                answers.remove(None)
            answer = (
                node.val + max(answers, default=0)
            )
            # print(f'max({VAL(node)}): {answer}')
            return answer

        if not root:
            # print(f'sSub({VAL(root)},{limit}) -> None')
            return None
        
        maxSum = maxSumToLeaf(root)

        if maxSum < limit:
            # print(f'sSub({VAL(root)},{limit}) -> None')
            return None
        
        # print(f'sSub({VAL(root)}({VAL(root.left)},{VAL(root.right)}),{limit}):before')
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        # print(f'sSub({VAL(root)}({VAL(root.left)},{VAL(root.right)}),{limit}):after')
        return root

# NOTE: Accepted on second Run (first was using 0 as minimum sum)
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 319 ms Beats 5.94%
# NOTE: Memory 24.22 MB Beats 9.11%
