# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        DEBUG = False

        nodes_by_string = {}    # Dict[str,List[TreeNode]]
        def file_all_nodes_by_string(node: TreeNode, depth=0) -> str:
            nonlocal nodes_by_string
            margin = ' ' * depth
            if node is None:
                return '-'
            Left = file_all_nodes_by_string(node.left, depth+1)
            Right = file_all_nodes_by_string(node.right, depth+1)
            Answer = f'({node.val} L:{Left} R:{Right})'
            Answer = Answer.replace(' L:-', '')
            Answer = Answer.replace(' R:-', '')
            if DEBUG: print(f'{margin}{Answer}')
            nodes_by_string.setdefault(Answer, [])
            nodes_by_string[Answer].append(node)
            return Answer
        
        ignore = file_all_nodes_by_string(root)
        if DEBUG: print(f'ANSWERS:')
        answer = []
        for (toString, nodeList) in nodes_by_string.items():
            nodes = len(nodeList)
            if DEBUG: print(f'{nodes}: {toString}')
            if nodes > 1:
                if DEBUG: print(f'  YES')
                answer.append(nodeList[0])
            else:
                if DEBUG: print(f'  no')
        
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 49 ms Beats 47.23%
# NOTE: Memory 28.04 MB Beats 25.31%
