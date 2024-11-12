
        def sizeOfSubtree(node: TreeNode) -> int:
            if not node:
                return 0
            return sum([
                sizeOfSubtree(node.left),
                sizeOfSubtree(node.right),
            ]) + 1

