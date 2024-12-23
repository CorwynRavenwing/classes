class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        grid = mat  # variable rename
        
        # I've read the hints, and they sound crazy, because they will miss
        # lots of test cases, e.g. where the highest value in one row is
        # adjacent to a higher value in the next row, but a second, less-high
        # local peak on this row (with lower values on the next row, therefore
        # the correct answer) will be ignored.  Therefore I'm ignoring the hints.

        M = len(grid)
        N = len(grid[0])

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

        def getValue(cell: Tuple[int,int]) -> int:
            # special treatment of out-of-bounds values:
            if OOB(cell):
                return -1
            (X, Y) = cell
            return grid[X][Y]
        
        def is_peak(cell: Tuple[int,int]) -> int:
            value = getValue(cell)
            for neighbor in neighborsOf(cell):
                neighbor_val = getValue(neighbor)
                if neighbor_val > value:
                    return False
            return True

        for X in range(M):
            for Y in range(N):
                cell = (X, Y)
                if is_peak(cell):
                    return cell
        
        print(f'Found no peak cells!')
        return [-99,-99]

# NOTE: Accepted on second Run (variable-rename required)
# NOTE: Accepted on first Submit
# NOTE: Runtime 431 ms Beats 5.17%
# NOTE: Memory 46.08 MB Beats 8.03%
