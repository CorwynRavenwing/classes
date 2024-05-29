# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def NodesByInfix(node: Optional[TreeNode]) -> List[TreeNode]:
            if node is None:
                return []
            return NodesByInfix(node.left) + [node] + NodesByInfix(node.right)
        
        def ShowNodeList(nodes: List[TreeNode]) -> List[int]:
            answer = [
                N.val
                for N in nodes
            ]
            return answer
        
        nodes_infix = NodesByInfix(root)
        nodes_value = sorted(
            nodes_infix,
            key=lambda x: x.val
        )
        print(f'infix={ShowNodeList(nodes_infix)}')
        print(f'value={ShowNodeList(nodes_value)}')
        
        nodes_diff = [
            (A, B)
            for (A, B) in zip(nodes_infix, nodes_value)
            if A != B
        ]
        for i, D in enumerate(nodes_diff):
            print(f'diff[{i}]={ShowNodeList(D)}')
        assert len(nodes_diff) == 2
        (diff1, diff2) = nodes_diff
        (A, B) = diff1
        (C, D) = diff2
        assert (A == D) and (B == C)
        (A.val, B.val) = (B.val, A.val)
        """
        Do not return anything, modify root in-place instead.
        """

