class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        # SHORTCUT: counting on the fact that battleships must
        # not be adjacent, *only* count "X" cells which have
        # either a "." cell, or an OOB, to the Left and Up of them.

        M = len(board)
        N = len(board[0])

        count = 0

        # case 1: UL corner
        if board[0][0] == 'X':
            print(f'1: (0,0)')
            count += 1
        
        # case 2: L column
        for X in range(1, M):
            if board[X][0] == 'X' and board[X-1][0] == '.':
                print(f'2: ({X},0)')
                count += 1

        # case 3: U row
        for Y in range(1, N):
            if board[0][Y] == 'X' and board[0][Y-1] == '.':
                print(f'3: (0,{Y})')
                count += 1

        # case 4: remainder
        for X in range(1, M):
            for Y in range(1, N):
                if board[X][Y] == 'X' and board[X-1][Y] == '.' and board[X][Y-1] == '.':
                    print(f'4: ({X},{Y})')
                    count += 1
        
        return count

# NOTE: Accepted on first Submit
# NOTE: Runtime 77 ms Beats 28.17%
# NOTE: O(M * N)
# NOTE: Memory 17.16 MB Beats 50.97%
# NOTE: O(1)
