class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        bishopDirections = (
            (-1, -1),
            (-1, +1),
            (+1, -1),
            (+1, +1),
        )
        rookDirections = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )

        def legalPos(pos: Tuple[int,int]) -> bool:
            (X, Y) = pos
            return (1 <= X <= 8) and (1 <= Y <= 8)
        
        def move(pos: Tuple[int,int], dir: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = pos
            (I, J) = dir
            return (X + I, Y + J)
        
        rook = (a, b)
        bishop = (c, d)
        queen = (e, f)

        # try each piece with each of his directions
        # continue move() until:
        # (A) == the other piece
        # (B) == queen
        # (C) not legalPos()

        def pieceCanTakeQueen(piecePos, pieceDirs, otherPiece, queen) -> bool:
            print(f'PCTQ({piecePos},{pieceDirs},{otherPiece},{queen})')
            for dir in pieceDirs:
                print(f'  {dir=}')
                pos = piecePos
                print(f'  {pos=}')
                while True:
                    pos = move(pos, dir)
                    print(f'    {pos=}')
                    if not legalPos(pos):
                        print(f'      OOB')
                        break
                    if pos == queen:
                        print(f'      YES')
                        return True
                    if pos == otherPiece:
                        print(f'      Hit other piece')
                        break
            print(f'NO')
            return False

        if pieceCanTakeQueen(rook, rookDirections, bishop, queen):
            return 1
        
        if pieceCanTakeQueen(bishop, bishopDirections, rook, queen):
            return 1

        # impossible to be more than 2
        return 2

# NOTE: Accepted on first Submit
# NOTE: Runtime 71 ms Beats 6.93%
# NOTE: Memory 16.68 MB Beats 18.61%
