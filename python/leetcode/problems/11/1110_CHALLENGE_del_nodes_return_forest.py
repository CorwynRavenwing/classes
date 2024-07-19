# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        forest = []     # List[TreeNode]
        def postNodeInForest(node: TreeNode) -> None:
            nonlocal forest
            if node is not None:
                forest.append(node)
            else:
                print(f'skipping nonexistent tree')
            return

        def handleNode(node: TreeNode) -> bool:
            # Return value signifies "delete me" to parent
            nonlocal to_delete
            # nonlocal postNodeInForest
            if node is None:
                return False
            
            deleteLeft = handleNode(node.left)
            if deleteLeft:
                node.left = None
            
            deleteRight = handleNode(node.right)
            if deleteRight:
                node.right = None
            
            if node.val in to_delete:
                print(f'Delete node {node.val}!')
                postNodeInForest(node.left)
                postNodeInForest(node.right)
                return True
            else:
                return False

        deleteRootNode = handleNode(root)
        if deleteRootNode:
            print(f'Deleting root node')
        else:
            postNodeInForest(root)
        
        return forest

