# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            # create a new node with no children
            return TreeNode(val)
        
        if root.val < val:
            # create a new root node with current tree as its left value
            return TreeNode(val, root, None)
        
        # replace current node's right value with a recursive call
        # to file 'val' somewhere right-and-below of this node
        root.right = self.insertIntoMaxTree(root.right, val)
        # then return current root with updated right value
        return root

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.68 MB Beats 30.82%
