# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # def find_inorder_next_value(root: TreeNode, value: int) -> int:
        #     xxxx

        def show(label: str, node: TreeNode) -> None:
            string = f'{label}: {node}'
            string = string.replace('TreeNode{val: ', '{')
            string = string.replace('left: ', 'L:')
            string = string.replace('right: ', 'R:')
            string = string.replace('L:None', '(L)')
            string = string.replace('R:None', '(R)')
            string = string.replace(', (L), (R)}', '}')
            print(string)
            return
        
        # 0. return immediately, if no root
        if not root:
            return root
        
        # 1. find the node, if it exists
        if root.val > key:
            print(f'  {root.val} > {key=}: LEFT')
            root.left = self.deleteNode(root.left, key)
            return root
        if root.val < key:
            print(f'  {root.val} < {key=}: RIGHT')
            root.right = self.deleteNode(root.right, key)
            return root
        if root.val == key:
            # 2. found: delete it
            print(f'  {root.val} == {key=}: DELETE')
            if (not root.left) and (not root.right):
                print(f'    No children: delete node as-is')
                return None
            if (not root.right):
                print(f'    No right node: return left')
                return root.left
            if (not root.left):
                print(f'    No left node: return right')
                return root.right
            if (root.left) and (root.right):
                print(f'    Both children: complicated')
                node = root.right
                while node.left:
                    node = node.left
                print(f'    -> inorder next == {node.val}')
                root.val = node.val
                # 3. cascade delete
                print(f'    -> recursive delete')
                root.right = self.deleteNode(root.right, node.val)
                return root

# NOTE: This version works much better than the prior
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 61 ms Beats 24.69%
# NOTE: Memory 20.01 MB Beats 17.04%
