# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def showNode(label: str, node: Optional[TreeNode]) -> None:
            text = f'{label} {node}'
            text = text.replace('TreeNode{val: ', '{')
            text = text.replace('left: None', '[L]')
            text = text.replace('right: None', '[R]')
            text = text.replace(', [L], [R]}', '}')
            print(text)
            return

        def min_max_check(node: TreeNode) -> Tuple[int,int]:
            if node.left:
                print(f'left')
                (left_min, left_max) = min_max_check(node.left)
                if None in [left_min, left_max]:
                    return (None,None)
                if left_max >= node.val:
                    return (None,None)
            else:
                left_min = node.val
            if node.right:
                print(f'right')
                (right_min, right_max) = min_max_check(node.right)
                if None in [right_min, right_max]:
                    return (None,None)
                if node.val >= right_min:
                    return (None,None)
            else:
                right_max = node.val
            return (left_min, right_max)
        
        showNode('IVB()', root)

        # if not root:
        #     print(f'YES: null root is BST')
        #     return True

        # print(f'IBV calling left')
        # if not self.isValidBST(root.left):
        #     print(f'NO: invalid left')
        #     return False
        # print(f'IBV calling right')
        # if not self.isValidBST(root.right):
        #     print(f'NO: invalid right')
        #     return False
        print(f'IBV callling MMC')
        MMV = min_max_check(root)
        if None in MMV:
            return False
        else:
            return True

