class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        def check_board(board: List[List[str]]) -> str:
            rows = [
                ''.join(row)
                for row in board
            ]
            print(f'{rows=}')
            board_zip = list(zip(*board))
            cols = [
                ''.join(col)
                for col in board_zip
            ]
            print(f'{cols=}')
            diags = [
                board[0][0] + board[1][1] + board[2][2],
                board[0][2] + board[1][1] + board[2][0],
            ]
            print(f'{diags=}')
            for player in 'A', 'B':
                win = player * 3
                if win in rows or win in cols or win in diags:
                    return player
            empty = [
                (i, j)
                for j, row in enumerate(board)
                for i, cell in enumerate(row)
                if cell == '.'
            ]
            print(f"{empty=}")
            if not empty:
                return 'Draw'
            return None

        print(f"{moves=}")
        board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        answer = check_board(board)
        print(f"check_board returned {answer}")
        if answer:
            return answer
        symbols = 'AB'
        player = 0
        for move in moves:
            symbol = symbols[player]
            print(f"{player=} {symbol=} {move=}")
            (i, j) = move
            board[i][j] = symbol
            answer = check_board(board)
            print(f"check_board returned {answer}")
            if answer:
                return answer
            player = (player + 1) % 2
        print("board at end:")
        print('\n'.join([
            ' '.join(row)
            for row in board
        ]))
        return 'Pending'

