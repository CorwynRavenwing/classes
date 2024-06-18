class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        tree = preorder.split(',')
        print(f'{tree}')

        def consumeTree(tree: List[str], depth=0) -> List[str]:
            margin = "  " * depth
            if not tree:
                # no root node: fail
                return None
            
            myself = tree.pop(0)
            print(margin + f'{myself}')
            if myself == '#':
                return tree
            print(margin + f'{myself}.left:')
            afterLeftTree = consumeTree(tree, depth + 1)
            print(margin + f'{myself}.right:')
            afterRightTree = consumeTree(afterLeftTree, depth + 1)
            return afterRightTree

        remain = consumeTree(tree)
        print(f'{remain=}')
        return (remain is not None) and (len(remain) == 0)

