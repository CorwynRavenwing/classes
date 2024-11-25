class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        solved = [[1,2,3],[4,5,0]]

        def make_immutable(board: List[List[int]]) -> List[List[int]]:
            return tuple(map(tuple, board))
        
        def make_mutable(board: List[List[int]]) -> List[List[int]]:
            return list(map(list, board))
        
        M = len(board)
        N = len(board[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            Neighbors = (
                (X + I, Y + J)
                for (I, J) in directions
            )
            return tuple([
                C
                for C in Neighbors
                if legalPos(C)
            ])

        def getValue(board: List[List[int]], cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return board[X][Y]

        # given a mutable board: return board with value changed
        def setValue(board: List[List[int]], cell: Tuple[int,int], value: int) -> List[List[int]]:
            (X, Y) = cell
            if OOB(cell):
                return False
            board[X][Y] = value
            return board
        
        # given an immutable board: return board with two values swapped (make temporarily mutable)
        def swapValues(board: List[List[int]], cell1: Tuple[int,int], cell2: Tuple[int,int]) -> List[List[int]]:
            board = make_mutable(board)
            v1 = getValue(board, cell1)
            v2 = getValue(board, cell2)
            setValue(board, cell1, v2)
            setValue(board, cell2, v1)
            board = make_immutable(board)
            return board
        
        def allCellsWithValue(board: List[List[int]], value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue(board, (X, Y)) == value
            ]

        board = make_immutable(board)
        solved = make_immutable(solved)

        zeroPosList = allCellsWithValue(board, 0)
        assert len(zeroPosList) == 1
        zeroPos = zeroPosList[0]
        seen = set()
        queue = {(board, zeroPos)}
        distance = 0
        while queue:
            newQ = set()
            for (board, zeroPos) in queue:
                if board in seen:
                    continue
                else:
                    seen.add(board)
                print(f'D={distance}: {board}')
                if board == solved:
                    print(f'  Solved!')
                    return distance
                for movePos in neighborsOf(zeroPos):
                    new_zero = movePos
                    new_board = swapValues(board, zeroPos, movePos)
                    if new_board in seen:
                        # skip if we've seen it already
                        continue
                    # print(f'  ->{new_board}')
                    newQ.add((new_board, new_zero))

            queue = newQ
            distance += 1
            print()
        
        return -1

# NOTE: Acceptance Rate 65.6% (HARD)
# NOTE: Accepted on third Run (small typos)
# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 18.78%
# NOTE: Memory 17.21 MB Beats 11.88%
