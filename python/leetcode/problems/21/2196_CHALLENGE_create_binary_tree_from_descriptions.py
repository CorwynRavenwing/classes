# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        NodesDict = {
            # parentValue: [leftChild, rightChild]
        }
        parentSet = set()
        childSet = set()
        for (parentI, childI, isLeftI) in descriptions:
            # print(f'({parentI=}, {childI=}, {isLeftI=})')
            NodesDict.setdefault(parentI, [None, None])
            index = (0 if isLeftI else 1)
            NodesDict[parentI][index] = childI
            # print(f'  ND[{parentI}]={NodesDict[parentI]}')
            parentSet.add(parentI)
            childSet.add(childI)
        
        # print(f'{NodesDict=}')
        # print(f'{parentSet=}')
        # print(f'{childSet=}')
        orphanSet = parentSet - childSet
        # print(f'{orphanSet=}')
        assert len(orphanSet) == 1
        rootVal = list(orphanSet).pop()
        # print(f'{rootVal=}')

        def createTreeNode(parentVal: int, depth=0) -> TreeNode:
            margin = '  ' * depth
            # print(f'{margin}CTN({parentVal})')
            nonlocal NodesDict
            try:
                children = NodesDict[parentVal]
                childNodes = [
                    (
                        createTreeNode(childVal, depth + 1)
                        if childVal is not None
                        else None
                    )
                    for childVal in children
                ]
            except KeyError:
                childNodes = [None, None]
            return TreeNode(parentVal, *childNodes)

        return createTreeNode(rootVal)

