# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelValues(self, nodes: List[TreeNode]) -> List[int]:
        values = [
            node.val
            for node in nodes
            if node
        ]
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

    # this version of levelOrder returns the actual nodes themselves,
    # rather than their values:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[TreeNode]]:
        nodes = [root]
        answer = []
        while nodes:
            answer.append(nodes)
            nodes = self.nextLevel(nodes)
        if [] in answer:
            answer.remove([])

        return answer

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        LevelOrder = self.levelOrder(root)
        # print(f'{LevelOrder=}')

        sizes = tuple(map(len, LevelOrder))
        print(f'{sizes=}')

        size_is_2_pow_H = [
            size == 2 ** H
            for H, size in enumerate(sizes)
        ]
        print(f'{size_is_2_pow_H=}')

        if all(size_is_2_pow_H):
            return True
        
        if not all(size_is_2_pow_H[:-1]):
            return False
        
        def check_children(node: TreeNode) -> str:
            if not node:
                return '0'
            if node.left and node.right:
                return 'B'
            if node.left and (not node.right):
                return 'L'
            if (not node.left) and node.right:
                return 'R'
            if (not node.left) and (not node.right):
                return 'X'
            raise Exception(f'Logic error: {node=} does not match any patterns')

        second_last_row = LevelOrder[-2]
        print(f'{second_last_row=}')
        children = list(map(check_children, second_last_row))
        print(f'{children=}')

        if 'R' in children:
            return False
        
        while children and (children[0] == 'B'):
            # first set of nodes may be 'Both'
            del children[0]

        while children and (children[-1] == 'X'):
            # last set of nodes may be 'Neither'
            del children[-1]

        if (not children) or (children == ['L']):
            # only remaining child may be 'Left'
            # or, there may be no remaining children
            return True

        # any other case is non-complete
        print(f'Non-complete: leftover {children=}')
        return False

# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 94.96%
# NOTE: Memory 16.72 MB Beats 11.13%
