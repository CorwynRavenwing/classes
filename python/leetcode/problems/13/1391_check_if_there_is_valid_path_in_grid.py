class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        grid_M = len(grid)
        grid_N = len(grid[0])
        origin = (0, 0)
        target = (grid_M - 1, grid_N - 1)

        def legalPos(cell: Tuple[int,int]) -> bool:
            nonlocal grid_M, grid_N
            (X, Y) = cell
            return (0 <= X < grid_M) and (0 <= Y < grid_N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        neighborCache = {}
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            if OOB(cell):
                return []
            if cell in neighborCache:
                return neighborCache[cell]
            (X, Y) = cell
            street = grid[X][Y]
            # print(f'{cell=} -> {street=}')
            U = (X - 1, Y)
            D = (X + 1, Y)
            L = (X, Y - 1)
            R = (X, Y + 1)
            answer = []
            match street:
                case 1:
                    answer = (L, R)
                case 2:
                    answer = (U, D)
                case 3:
                    answer = (L, D)
                case 4:
                    answer = (R, D)
                case 5:
                    answer = (U, L)
                case 6:
                    answer = (U, R)
            neighborCache[cell] = answer
            return answer

        def connectedCells(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            retval = [
                N
                for N in neighborsOf(cell)  # I'm connected to him
                if cell in neighborsOf(N)   # he's connected back to me
            ]
            return retval
        
        seen = set()
        possibles = {origin}
        while possibles:
            new_possibles = set()
            for P in possibles:
                if P in seen:
                    # print(f'  -> seen')
                    continue
                print(f'{P=}')
                seen.add(P)
                if P == target:
                    print(f'  -> DONE')
                    return True
                for C in connectedCells(P):
                    if C not in seen:
                        # print(f'  {C=}')
                        new_possibles.add(C)
            possibles = new_possibles
        print(f'FAIL')
        return False

