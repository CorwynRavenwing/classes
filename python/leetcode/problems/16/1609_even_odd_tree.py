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

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        EVEN = lambda X: (X % 2 == 0)
        ODD = lambda X: not EVEN(X)

        ALL_EVEN = lambda L: all(map(EVEN, L))
        ALL_ODD = lambda L: all(map(ODD, L))

        REV = lambda L: tuple(reversed(tuple(L)))

        DESC = lambda L: all([A > B for A, B in pairwise(L)])
        ASC = lambda L: DESC(REV(L))

        levelOrderData = self.levelOrder(root)
        for level, levelValues in enumerate(levelOrderData):
            if EVEN(level):
                if not ALL_ODD(levelValues):
                    return False
                if not ASC(levelValues):
                    return False
            elif ODD(level):
                if not ALL_EVEN(levelValues):
                    return False
                if not DESC(levelValues):
                    return False
            else:
                raise Exception(f'Error: {level} is neither EVEN nor ODD')
        
        return True

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 199 ms Beats 5.19%
# NOTE: Memory 44.81 MB Beats 15.35%
