# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print(f'LCA(node:{root.val},P:{p.val},Q:{q.val})')
        if p == root or q == root:
            print(f'  Match this node (P/Q)')
            return root
        if p.val > q.val:
            (p, q) = (q, p)
        if p.val <= q.val < root.val:
            print(f'  Left side')
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val <= q.val:
            print(f'  Right side')
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val < q.val:
            print(f'  Match this node (between)')
            return root
        raise ValueError(f'ERROR:\n{root=}\n{p=}\n{q=}')

# NOTE: Accepted on first Submit
# NOTE: Runtime 50 ms Beats 83.68%
# NOTE: Memory 20.58 MB Beats 5.29%
