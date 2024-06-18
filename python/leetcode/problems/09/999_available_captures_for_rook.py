class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        H = len(board)
        W = len(board[0])
        print(f"{H=},{W=}")

        def move(T, D):
            (i, j) = T
            (x, y) = D
            return (i+x, j+y)

        def legal_position(T):
            (i, j) = T
            return (0 <= i < W) and (0 <= j < H)

        pieces = {
            (i, j): P
            for j, row in enumerate(board)
            for i, P in enumerate(row)
            if P != '.'
        }
        print(f"{pieces=}")
        rook = [
            (i, j)
            for (i, j), P in pieces.items()
            if P == 'R'
        ]
        assert len(rook) == 1
        rook = rook.pop()
        print(f'{rook=}')
        answer = 0
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            pos = rook
            print(f"{pos}: R +{direction}")
            while True:
                pos = move(pos, direction)
                if not legal_position(pos):
                    print(f"{pos}: OOB")
                    break
                elif pos in pieces:
                    piece = pieces[pos]
                    if piece == 'B':
                        print(f"{pos}: {piece}")
                        break
                    elif piece == 'p':
                        print(f"{pos}: {piece} CAPTURE")
                        answer += 1
                        break
                    else:
                        print(f"{pos}: {piece}: ERROR!")
                        raise Exception(f"invalid piece '{pos}'")
                else:
                    print(f"{pos}: -")

        return answer

