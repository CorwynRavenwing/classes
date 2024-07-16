# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findPathTo(node: TreeNode, value: int) -> str:
            
            if node is None:
                return None
            
            if node.val == value:
                return ''
            
            LeftPath = findPathTo(node.left, value)
            if LeftPath is not None:
                return 'L' + LeftPath
            
            RightPath = findPathTo(node.right, value)
            if RightPath is not None:
                return 'R' + RightPath
            
            return None
        
        startPath = findPathTo(root, startValue)
        destPath = findPathTo(root, destValue)

        print(f'{startPath[:20]=}...')
        print(f'{destPath[:20]=}...')

        while startPath and destPath and startPath[0] == destPath[0]:
            startPath = startPath[1:]
            destPath = destPath[1:]
        
        fromStart = 'U' * len(startPath)
        return fromStart + destPath

