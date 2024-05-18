from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_row(row: List[str]) -> bool:
            count_row = Counter(row)
            if '.' in row:
                del count_row['.']
            # print(f'{count_row=}')
            for val, count in count_row.items():
                if count > 1:
                    print(f'  found {count}(>1) "{val}"')
                    return False
            return True

        for row in board:
            print(f'{row=}')
            ans = check_row(row)
            # print(f'  {ans=}')
            if not ans:
                return False
        
        reverse_board = list(zip(*board))
        for col in reverse_board:
            print(f'{col=}')
            ans = check_row(col)
            # print(f'  {ans=}')
            if not ans:
                return False

        def board_blocks(board: List[List[str]]) -> List[List[str]]:

            def board_block(board: List[List[str]], x: int, y: int) -> List[str]:
                rows = board[x * 3:(x + 1) * 3]
                # print(f'board[{x * 3}:{(x + 1) * 3}]')
                # print(f'  {rows=}')
                # print(f'row[{y * 3}:{(y + 1) * 3}]')
                cols = [
                    row[y * 3:(y + 1) * 3]
                    for row in rows
                ]
                # print(f'  {cols=}')
                return cols[0] + cols[1] + cols[2]

            return [
                board_block(board, x, y)
                for x in range(3)
                for y in range(3)
            ] 
        
        blocks = board_blocks(board)
        for blk in blocks:
            print(f'{blk=}')
            ans = check_row(blk)
            # print(f'  {ans=}')
            if not ans:
                return False
        
        return True

