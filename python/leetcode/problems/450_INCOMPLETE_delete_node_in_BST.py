# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def show(label: str, node: TreeNode) -> None:
            string = f'{label}: {node}'
            string = string.replace('TreeNode{val: ', '{')
            string = string.replace('left: ', 'L:')
            string = string.replace('right: ', 'R:')
            string = string.replace('L:None', '(L)')
            string = string.replace('R:None', '(R)')
            string = string.replace(', (L), (R)}', '}')
            print(string)
            return
        
        # 0. return immediately, if no root
        if not root:
            return root
        
        # 1. find the node, if it exists
        node = root
        parent = None
        side = None
        while True:
            show('check node', node)
            if node.val == key:
                print(f'FOUND')
                node.val = None
                show('found node', node)
                show('found parent', parent)
                show('found side', side)
                break
            elif node.val > key:
                parent = node
                side = 'left'
                node = node.left
                show('parent', parent)
                show('left', node)
                show('side', side)
            elif node.val < key:
                parent = node
                side = 'right'
                node = node.right
                show('parent', parent)
                show('right', node)
                show('side', side)
            if not node:
                print(f'not found')
                break

        # 2. delete that node, if it exists
        while node:
            show('delete node', node)
            if (node.left) and (node.right):
                print(f'both left and right exist')
                if (not node.left.right):
                    print(f'overwrite node(L): {node.val} <- {node.left.val}')
                    node.val = node.left.val
                    node.left.val = None
                    parent = node
                    side = 'left'
                    node = node.left
                    show('del parent', parent)
                    show('del left', node)
                    show('del side', side)
                    continue
                if (not node.right.left):
                    print(f'overwrite node(R): {node.val} <- {node.right.val}')
                    node.val = node.right.val
                    node.right.val = None
                    parent = node
                    side = 'right'
                    node = node.right
                    show('del parent', parent)
                    show('del right', node)
                    show('del side', side)
                    continue
                else:
                    print(f'both left.right and right.left exist')
                    # arbitrarily choose to go down the left path here.
                    nextparent = node
                    nextnode = node.left
                    nextside = None
                    while nextnode and nextnode.right:
                        nextparent = nextnode
                        nextnode = nextnode.right
                        nextside = 'right'
                    show('LRRR node', nextnode)
                    show('LRR parent', nextparent)
                    show('LRR side', nextside)

                    print(f'overwrite node(LRRR): {node.val} <- {nextnode.val}')
                    node.val = nextnode.val
                    nextnode.val = None
                    parent = nextparent
                    side = nextside
                    node = nextnode
                    show('del LRR parent', parent)
                    show('del LRRR node', node)
                    show('del LRR side', side)
                    continue
                continue

            if (node.left) and (not node.right):
                print(f'overwrite node(L): {node.val} <- {node.left.val}')
                node.val = node.left.val
                node.left.val = None
                parent = node
                side = 'left'
                node = node.left
                show('del parent', parent)
                show('del left', node)
                show('del side', side)
                continue

            if (node.right) and (not node.left):
                print(f'overwrite node(R): {node.val} <- {node.right.val}')
                node.val = node.right.val
                node.right.val = None
                parent = node
                side = 'right'
                node = node.right
                show('del parent', parent)
                show('del right', node)
                show('del side', side)
                continue

            # node has no children here
            assert (not node.left) and (not node.right)

            if not parent:
                print(f'node has no children: also, no parent: delete root')
                show('delete root: parent', parent)
                show('delete root: node', node)
                show('delete root: side', side)
                # should unmalloc(node) here
                root = None
                node = None
            else:
                print(f'node has no children: delete from parent')
                show('deleting: parent', parent)
                show('deleting: parent.left', parent.left)
                show('deleting: parent.right', parent.right)
                show('deleting: node', node)
                show('deleting: side', side)
                if not parent:
                    print(f'error, "parent" not set here')
                    break
                else:
                    if side is None:
                        print(f'error, "side" is not set here')
                        break
                    elif side == 'left':
                        if node != parent.left:
                            print('error, parent.left != this node')
                            break
                        else:
                            parent.left = None
                            # should unmalloc(node) here
                            node = None
                    elif side == 'right':
                        if node != parent.right:
                            print('error, parent.right != this node')
                            break
                        else:
                            parent.right = None
                            # should unmalloc(node) here
                            node = None

        # 3. return root, possibly updated
        show('returning root', root)
        return root

# NOTE: test case 83 is failing
# NOTE: try translating it into an array in L-C-R notation, to verify
#   that none of our changes are ruining the BST ordering

