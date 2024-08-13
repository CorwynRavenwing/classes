# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # SHORTCUT: since "cousins" is defined as "descendents at my
        # level who aren't my siblings", we can define "sum of my cousins'
        # values" as "sum of my entire level, minus me and my sibling's sum"

        sumByLevel = {}
        def setSumByLevel(node: TreeNode, level=0) -> None:
            if node is None:
                return
            sumByLevel.setdefault(level, 0)
            sumByLevel[level] += node.val
            setSumByLevel(node.left, level+1)
            setSumByLevel(node.right, level+1)
            return
        setSumByLevel(root)
        print(f'{sumByLevel=}')

        def replaceValue(node: TreeNode, siblingSum: int, level=0) -> None:
            if node is None:
                return
            node.val = sumByLevel[level] - siblingSum
            childrenSum = (
                (
                    node.left.val
                    if node.left is not None
                    else 0
                ) + (
                    node.right.val
                    if node.right is not None
                    else 0
                )
            )
            replaceValue(node.left, childrenSum, level+1)
            replaceValue(node.right, childrenSum, level+1)
            return
        
        replaceValue(root, sumByLevel[0])
        return root
# NOTE: Runtime 621 ms Beats 44.61%
# NOTE: Memory 83.84 MB Beats 14.50%
