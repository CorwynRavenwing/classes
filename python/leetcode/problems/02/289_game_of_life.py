class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # SHORTCUT: we can't just overwrite the cells one at a time
        # because the later calculations will be based on our new value
        # rather than (properly) on the old value.
        # Instead, we set "true next time" by adding 2 to the cell value,
        # and query each cell modulo 2, which filters out the "next time" value
        
        m = len(board)
        n = len(board[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < m) and (0 <= Y < n)

        directions = {
            (I, J)
            for I in [-1, 0, 1]
            for J in [-1, 0, 1]
            if (I, J) != (0, 0)
        }

        def valueAt(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return board[X][Y] % 2

        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            answer = {
                (X + I, Y + J)
                for (I, J) in directions
            }
            return {
                P
                for P in answer
                if legalPos(P)
            }
        
        def liveNeighbors(cell: Tuple[int,int]) -> int:
            return sum([
                valueAt(pos)
                for pos in neighborsOf(cell)
            ])

        for i, row in enumerate(board):
            # print(f'{i=}')
            for j, val in enumerate(row):
                # print(f'  {j=}')
                Neighbors = liveNeighbors((i, j))
                Live = (val % 2)
                # print(f'    {val=} {Live=} {Neighbors=}')
                Live_next = (
                    Live and Neighbors in [2, 3]
                ) or (
                    not Live and Neighbors in [3]
                )
                if Live_next:
                    # print(f'      New cell is Live')
                    board[i][j] += 2

        for i, row in enumerate(board):
            # print(f'{i=}')
            for j, val in enumerate(row):
                # print(f'  {j=}')
                board[i][j] //= 2
                # print(f'    {val} -> {board[i][j]}')
        
        return

# NOTE: Accepted on first Submit
# NOTE: Runtime 37 ms Beats 54.84%
# NOTE: Memory 16.74 MB Beats 18.24%
