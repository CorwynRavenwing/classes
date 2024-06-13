class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def boardWinner(board: List[str]) -> str:
            answer = ''
            lines = board.copy()
            for column in zip(*board):
                lines.append(''.join(column))
            lines.extend([
                board[0][0] + board[1][1] + board[2][2],
                board[0][2] + board[1][1] + board[2][0],
            ])
            print(f'{lines=}')
            if 'XXX' in lines:
                answer += 'X'
            if 'OOO' in lines:
                answer += 'O'
            if answer == 'XO':
                answer = '!'
            return answer
        
        def boardLastPlayer(board: List[str]) -> str:
            flatten = ''.join(board)
            counts = Counter(flatten)
            print(f'{counts=}')
            Xs = counts['X']
            Os = counts['O']
            if Xs == 0 and Os == 0:
                return ''
            if Xs == Os:
                return 'O'
            if Xs == Os + 1:
                return 'X'
            print(f'Invalid number of {Xs=} and {Os=}')
            return '!'
            pass
        
        winner = boardWinner(board)
        if winner == '!':
            return False
        
        lastPlayer = boardLastPlayer(board)
        if lastPlayer == '!':
            return False
        if lastPlayer == '':
            return True
        if winner:
            if lastPlayer != winner:
                print(f'mismatch between "{lastPlayer}" and "{winner}"')
                return False
        
        return True
# NOTE: 27 ms; Beats 95.26% of users with Python3
