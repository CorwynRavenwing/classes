# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print(f'iiBST({root.val if root else None},{val})')

        if not root:
            return TreeNode(val)
        
        if val < root.val:
            # insert on left
            root.left = self.insertIntoBST(root.left, val)
            return root
        
        if root.val < val:
            # insert on right
            root.right = self.insertIntoBST(root.right, val)
            return root
        
        raise Exception(f'Logic error: {val=} <=> {self.val=}')
        return None

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 85 ms Beats 45.42%
# NOTE: Memory 18.69 MB Beats 62.24%
