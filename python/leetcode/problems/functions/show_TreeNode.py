
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

