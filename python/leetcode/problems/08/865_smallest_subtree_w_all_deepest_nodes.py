# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # @cache
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return sum([
            max([
                self.depth(root.left),
                self.depth(root.right),
            ]),
            1,
        ])

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def TreeNode_toString(node: TreeNode) -> str:
            S = f'{node}'
            S = S.replace('TreeNode{val: ', 'Tree{')
            S = S.replace(', left: ', ' L:')
            S = S.replace(', right: ', ' R:')
            S = S.replace('L:Tree{', 'L:{')
            S = S.replace('R:Tree{', 'R:{')
            S = S.replace(' L:None', ' L:-')
            S = S.replace(' R:None', ' R:-')
            S = S.replace(' L:- R:-}', '}')
            return S

        def show_TreeNode(label: str, node: TreeNode):
            nodeStr = TreeNode_toString(node)
            print(f'{label}: {nodeStr}')

        show_TreeNode('CALL', root)

        left = self.depth(root.left)
        right = self.depth(root.right)

        print(f'  {left=} {right=}')
        
        if left > right:
            print(f'    left bigger')
            # left bigger
            return self.subtreeWithAllDeepest(root.left)
            
        if left < right:
            print(f'    right bigger')
            # right bigger
            return self.subtreeWithAllDeepest(root.right)
        
        if left == right:
            print(f'    equal')
            # equal
            return root
        
        raise Exception(f'Error: cannot compare {left=} <=> {right=}')

# NOTE: Accepted on first Submit
# NOTE: Runtime 36 ms Beats 64.40%
# NOTE: Memory 16.96 MB Beats 9.38%
