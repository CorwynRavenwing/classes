# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def show_TreeNode(label: str, node: TreeNode):
            return
            S = f'{label}: {node}'
            S = S.replace('TreeNode{val: ', 'Tree{')
            S = S.replace(', left: ', ' L:')
            S = S.replace(', right: ', ' R:')
            S = S.replace('L:Tree{', 'L:{')
            S = S.replace('R:Tree{', 'R:{')
            S = S.replace(' L:None', ' L:-')
            S = S.replace(' R:None', ' R:-')
            S = S.replace(' L:- R:-}', '}')
            print(S)

        def addOneRecursive(node: TreeNode, val: int, depth: int, isLeft: bool, level=0) -> TreeNode:
            margin = ' ' * level
            show_TreeNode(f'{margin}a1R({val},{depth},{isLeft})', node)
            if depth == 1:
                if isLeft:
                    # original node goes to left side
                    node = TreeNode(val, node, None)
                else:
                    # original node goes to right side
                    node = TreeNode(val, None, node)
                show_TreeNode(f'{margin}:D1({val},{depth},{isLeft})', node)
                return node
            else:
                if node is None:
                    return None
                node.left = addOneRecursive(node.left, val, depth - 1, True, level+1)
                node.right = addOneRecursive(node.right, val, depth - 1, False, level+1)
                show_TreeNode(f'{margin}:R({val},{depth},{isLeft})', node)
                return node
        
        return addOneRecursive(root, val, depth, True)

# NOTE: Accepted on second Submit (first was Timeout: print less)
# NOTE: Runtime 64 ms Beats 6.12%
# NOTE: Memory 19.55 MB Beats 5.26%
