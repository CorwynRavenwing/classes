"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def showNode(self, node: 'Node') -> str:
        if not node:
            return '-'
        else:
            OC = '{'
            CC = '}'
            LEFT = self.showNode(node.left)
            RIGHT = self.showNode(node.right)
            NEXT = f'({node.next.val})' if node.next else "(-)"
            return f'{OC}{node.val}: {NEXT} L:{LEFT} R:{RIGHT}{CC}'

    def connect(self, root: 'Node') -> 'Node':
        print(f'connect({self.showNode(root)})')
        
        # we borrow some code from #116:

        # COMMENT: the major difference between this version and the prior
        # is that the tree is not "perfect": this means that we don't always
        # have both a Right and Left link.

        if not root:
            return root

        if root.left and root.right:
            root.left.next = root.right
        
        if root.left or root.right:
            NEXT = None
            PARENT = root.next
            while PARENT:
                print(f'Try setting Next to children of ({PARENT.val})')
                if PARENT.left:
                    NEXT = PARENT.left
                    break
                elif PARENT.right:
                    NEXT = PARENT.right
                    break
                else:
                    PARENT = PARENT.next
                    continue
            if root.right:
                root.right.next = NEXT
            elif root.left:
                root.left.next = NEXT
        
        # do Right first, so the PARENT.NEXT data is there when Left needs it
        self.connect(root.right)
        self.connect(root.left)

        return root

# NOTE: Used the prior version's code, with a few changes
# NOTE: Runtime 120 ms Beats 5.30%
# NOTE: Memory 17.74 MB Beats 8.40%
