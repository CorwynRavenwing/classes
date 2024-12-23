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

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        LO = self.levelOrder(root)
        # print(f'{LO=}')
        
        answer = 0
        for level in LO:
            if len(level) <= 1:
                continue
            print(f'{level=}')
            value_index_pairs = [
                (V, I)
                for I, V in enumerate(level)
            ]
            # print(f'start  {value_index_pairs=}')
            value_index_pairs.sort()
            # print(f'sorted {value_index_pairs=}')
            indexes = [
                I
                for V, I in value_index_pairs
            ]
            # print(f'{indexes=}')
            for i in range(len(indexes)):
                A = indexes[i]
                if A != i:
                    j = indexes.index(i, i + 1)     # use bisect instead?
                    print(f'  Swap {i} -> {j}')
                    B = indexes[j]
                    assert B == i
                    indexes[j] = A
                    indexes[i] = B
                    assert indexes[i] == i
                    answer += 1

        return answer

# NOTE: Accepted on second Run (constant typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 5343 ms Beats 11.11%
# NOTE: Memory 50.63 MB Beats 10.46%
