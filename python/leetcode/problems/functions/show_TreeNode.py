
        def TreeNode_toString(node: TreeNode) -> str:
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

        def show_TreeNode(label: str, node: TreeNode):
            nodeStr = TreeNode_toString(node)
            print(f'{label}: {nodeStr}')

        def show_TreeNode_List(label: str, subLabel: str, nodeList: List[TreeNode]):
            print(f'{label}:')
            if subLabel:
                subLabel += ' '
            for i, node in enumerate(nodeList):
                show_TreeNode(f'  {subLabel}{i}', node)
            return

# class version:

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

