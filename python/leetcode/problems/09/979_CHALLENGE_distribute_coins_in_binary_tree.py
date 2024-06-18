# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countCoinsAndNodes(self, root: Optional[TreeNode]) -> Tuple[int,int]:
        if not root:
            return (0, 0)
        
        (LC, LN) = self.countCoinsAndNodes(root.left)
        (RC, RN) = self.countCoinsAndNodes(root.right)

        return (
            LC + RC + root.val,
            LN + RN + 1
        )

    def showProgress(self, depth: int, label: str, moves: int, root: Optional[TreeNode]) -> None:
        show = f'{label} {moves=} {root=}'
        show = show.replace('left: None', '(left)')
        show = show.replace('right: None', '(right)')
        show = show.replace(', (left), (right)', '')
        print(show)
    
    def distributeCoins(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return 0
        
        moves = 0
        self.showProgress(depth, 'A', moves, root)
        (C, N) = self.countCoinsAndNodes(root)

        if (C, N) == (1, 1):
            print(f'  {(C, N)=}')
            return 0

        print(f'Total {C=} {N=}')
        # assert C == N

        (LC, LN) = self.countCoinsAndNodes(root.left)
        (RC, RN) = self.countCoinsAndNodes(root.right)

        change = (LC - LN)
        print(f'{change=} ({LC=} {LN=})')
        if change:
            print(f'  b {moves=} {root.val=} {root.left.val=}')
            moves += abs(change)
            root.left.val -= change
            root.val += change
            print(f'  a {moves=} {root.val=} {root.left.val=}')
            self.showProgress(depth,'B', moves, root)
        moves += self.distributeCoins(root.left)
        self.showProgress(depth,'C', moves, root)

        change = (RC - RN)
        print(f'{change=} ({RC=} {RN=})')
        if change:
            print(f'  b {moves=} {root.val=} {root.right.val=}')
            moves += abs(change)
            root.right.val -= change
            root.val += change
            print(f'  a {moves=} {root.val=} {root.right.val=}')
            self.showProgress(depth,'D', moves, root)
        moves += self.distributeCoins(root.right)
        self.showProgress(depth,'E', moves, root)
        
        (LC, LN) = self.countCoinsAndNodes(root.left)
        (RC, RN) = self.countCoinsAndNodes(root.left)

        if LC != LN:
            print(f'ERROR: Left {LC} != {LN}')
        if RC != RN:
            print(f'ERROR: Right {RC} != {RN}')

        self.showProgress(depth,'F', moves, root)
        return moves

