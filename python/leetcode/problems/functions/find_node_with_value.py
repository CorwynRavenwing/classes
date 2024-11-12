        def findNodeWithValue(node: TreeNode, value: int) -> TreeNode:
            if not node:
                return None
            if node.val == value:
                return node
            Left = findNodeWithValue(node.left, value)
            Right = findNodeWithValue(node.right, value)

            return (Left if Left else Right)

