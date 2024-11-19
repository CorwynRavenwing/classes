# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelValues(self, nodes: List[TreeNode]) -> List[int]:
        # print(f'>>{nodes=}')
        values = [
            node.val
            for node in nodes
            if node
        ]
        # print(f'<<{values=}')
        return values

    def nextLevel(self, nodes: List[TreeNode]) -> List[TreeNode]:
        newNodes = [
            [node.left, node.right]
            for node in nodes
            if node
        ]
        answer = [
            node
            for group in newNodes
            for node in group
            if node
        ]
        return answer

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = [root]
        answer = []
        while nodes:
            # print(f'{nodes=}')
            answer.append(
                self.levelValues(nodes)
            )
            nodes = self.nextLevel(nodes)
        # print(f'{answer=}')
        if [] in answer:
            answer.remove([])

        return answer

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level_order = self.levelOrder(root)
        last_level = level_order[-1]
        return sum(last_level)

# NOTE: re-used Level Order Traverse, with a little glue code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 28.66%
# NOTE: Memory 19.91 MB Beats 8.62%
