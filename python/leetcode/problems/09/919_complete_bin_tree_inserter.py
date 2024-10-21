# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def TreeNode_toString(self, node: TreeNode) -> str:
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

    def show_TreeNode(self, label: str, node: TreeNode):
        nodeStr = self.TreeNode_toString(node)
        print(f'{label}: {nodeStr}')
        return

    def show_TreeNode_List(self, label: str, subLabel: str, nodeList: List[TreeNode]):
        print(f'{label}:')
        if subLabel:
            subLabel += ' '
        for i, node in enumerate(nodeList):
            self.show_TreeNode(f'  {subLabel}{i}', node)
        return

    def __first_opening(self) -> TreeNode:

        print(f'__first_opening()')
        thisRow = [self.Root]
        while thisRow:
            # self.show_TreeNode_List('  thisRow', '  ', thisRow)
            nextRow = []
            for node in thisRow:

                if not node.left:
                    return node

                if not node.right:
                    return node
                
                nextRow.append(node.left)
                nextRow.append(node.right)
                # self.show_TreeNode_List('  nextRow', '  ', nextRow)

            thisRow = nextRow

        raise Exception(f'Error: {thisRow=} is empty, but we did not find any openings')

    def __init__(self, root: Optional[TreeNode]):
        # self.show_TreeNode(f'init()', root)
        self.Root = root
        return

    def insert(self, val: int) -> int:
        print(f'insert({val})')
        newNode = TreeNode(val)
        insertPoint = self.__first_opening()
        if not insertPoint.left:
            insertPoint.left = newNode
        elif not insertPoint.right:
            insertPoint.right = newNode
        else:
            raise Exception(f'__first_opening() returns {insertPoint=}, which has no opening')
        
        return insertPoint.val

    def get_root(self) -> Optional[TreeNode]:
        print(f'get_root()')
        return self.Root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

# NOTE: Runtime 80 ms Beats 20.11%
# NOTE: Memory 17.82 MB Beats 5.03%
