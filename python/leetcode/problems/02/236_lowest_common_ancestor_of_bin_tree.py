# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    @cache
    def isDescendantFound(self, root: 'TreeNode', p: 'TreeNode') -> bool:
        if not root:
            return False
        elif root == p:
            return True
        else:
            return any([
                self.isDescendantFound(root.left, p),
                self.isDescendantFound(root.right, p),
            ])

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # we borrow some code from #235:

        print(f'LCA({root.val},{p.val},{q.val})')
        if p == root or q == root:
            print(f'  Match this node (P/Q)')
            return root

        P_left = self.isDescendantFound(root.left, p)
        P_right = self.isDescendantFound(root.right, p)

        Q_left = self.isDescendantFound(root.left, q)
        Q_right = self.isDescendantFound(root.right, q)

        if P_left and Q_left:
            print(f'  Left side')
            return self.lowestCommonAncestor(root.left, p, q)
        if P_right and Q_right:
            print(f'  Right side')
            return self.lowestCommonAncestor(root.right, p, q)
        if (P_left and Q_right):
            print(f'  Match this node (P, Q)')
            return root
        if (Q_left and P_right):
            print(f'  Match this node (Q, P)')
            return root
        raise ValueError(f'ERROR:\n{root=}\n{p=}\n{q=}')

# NOTE: re-used most of the code from prior version
# NOTE: Accepted on first Submit
# NOTE: Runtime 104 ms Beats 5.51%
# NOTE: Memory 32.25 MB Beats 5.10%
