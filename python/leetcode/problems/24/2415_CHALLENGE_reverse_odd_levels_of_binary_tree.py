# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

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
            return
            nodeStr = TreeNode_toString(node)
            print(f'{label}: {nodeStr}')

        def swap_if_odd(node1: TreeNode, node2: TreeNode, isOdd: bool) -> None:

            if not node1:
                assert not node2
                return
            
            SHOW = lambda x: (x.val if x else "-")
            print(f'S({SHOW(node1)},{SHOW(node2)},{isOdd})')

            if isOdd:
                print(f'  (swap)')
                show_TreeNode('  before', root)
                (node1.val, node2.val) = (node2.val, node1.val)
                show_TreeNode('  after ', root)
            
            isEven = not isOdd
            swap_if_odd(node1.left, node2.right, isEven)
            if node1 == node2:
                return
            swap_if_odd(node1.right, node2.left, isEven)
            return
        
        show_TreeNode('start', root)
        swap_if_odd(root, root, False)
        show_TreeNode('end  ', root)
        return root
        
# NOTE: Accepted on second Run (duplicate work error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 94 ms Beats 7.68%
# NOTE: Memory 23.29 MB Beats 5.08%
