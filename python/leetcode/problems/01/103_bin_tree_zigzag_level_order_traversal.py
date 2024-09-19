# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # we borrow some code from #107:

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

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        REV = lambda x: tuple(reversed(tuple(x)))

        answer = [
            (
                level
                if index % 2 == 0
                else REV(level)
            )
            for index, level in enumerate(self.levelOrder(root))
        ]
        return answer

# NOTE: Reused all of prior version's code, only adding "reverse()"
# NOTE: Accepted on first Submit
# NOTE: Runtime 41 ms Beats 21.31%
# NOTE: Memory 16.83 MB Beats 6.68%
