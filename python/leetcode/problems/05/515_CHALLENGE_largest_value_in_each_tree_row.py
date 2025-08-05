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

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        valuesInLevelOrder = self.levelOrder(root)
        print(f'{valuesInLevelOrder=}')
        
        return tuple(map(max, valuesInLevelOrder))

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 55 ms Beats 5.09%
# NOTE: Memory 18.54 MB Beats 8.24%

# NOTE: re-ran for challenge:
# NOTE: [an error: return value can't be a map() -- fixed]
# NOTE: Runtime 5 ms Beats 9.78%
# NOTE: Memory 19.88 MB Beats 6.38%
