# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

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

        def show_TreeNode_List(label: str, subLabel: str, nodeList: List[TreeNode]):
            print(f'{label}:')
            if subLabel:
                subLabel += ' '
            for i, node in enumerate(nodeList):
                show_TreeNode(f'  {subLabel}{i}', node)
            return

        def MDNA(node: TreeNode, MinMaxAncestor=None) -> int:

            print(f'MDNA({MinMaxAncestor})', f'[{node.val if node else "-"}]')
            # show_TreeNode(f'MDNA({MinMaxAncestor})', node)

            if not node:
                print(f'  ->({MinMaxAncestor}): ', 0)
                return 0
            
            if MinMaxAncestor is None:
                MinMaxAncestor = (
                    float('+inf'),
                    float('-inf'),
                )
            
            (minAncestor, maxAncestor) = MinMaxAncestor
            newMinMaxAncestor = (
                min(minAncestor, node.val),
                max(maxAncestor, node.val),
            )
            myDiff = max([
                node.val - minAncestor,
                maxAncestor - node.val,
                MDNA(node.left, newMinMaxAncestor),
                MDNA(node.right, newMinMaxAncestor),
            ])
            print(f'  ->({MinMaxAncestor}): ', myDiff)
            return myDiff
        
        return MDNA(root)

# NOTE: Runtime 19 ms Beats 7.62%
# NOTE: Memory 19.46 MB Beats 5.69%
