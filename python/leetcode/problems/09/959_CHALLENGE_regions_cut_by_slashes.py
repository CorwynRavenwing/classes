class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        SP = ' '
        FS = '/'
        BS = '\\'
        print(f'"{SP}" "{FS}" "{BS}"')

        # THEY DID NOT ACTUALLY DO THE ESCAPING THEY CLAIMED THEY HAD DONE
        # THEREFORE UNDOING IT IS AN ERROR
        # # undo unnecessary escaping
        # print('\n'.join(grid))
        # grid = [
        #     row.replace(BS+BS, BS)
        #     for row in grid
        # ]
        # print('\n'.join(grid))

        grid_R = len(grid)
        grid_C = len(grid[0])

        # we declare a set of cells (R, C, Part)
        # where Part in ['T','B','L','R']
        # for all cells (R, C), new cell (R, C, 'T') connects to (R-1, C, 'B')
        # and (R, C, 'L') connects to (R, C-1, 'R').
        # in addition, internal to (R,C):
        # if '/', 'T' <-> 'L' and 'R' <-> 'B'
        # if '\'. 'T' <-> 'R' and 'L' <-> 'B'
        # if ' ', all four connect to each other.

        directions = {
            'T': (-1, 0),
            'B': (+1, 0),
            'L': (0, -1),
            'R': (0, +1),
        }
        opposites = {
            'T': 'B',
            'B': 'T',
            'L': 'R',
            'R': 'L',
        }
        adjacent = {
            SP: ['TBLR'],
            FS: ['TL', 'BR'],
            BS: ['TR', 'BL'],
        }

        def legalPos(subcell: Tuple[int,int,str]) -> bool:
            (R, C, ignore) = subcell
            return (0 <= R < grid_R) and (0 <= C < grid_C)
        
        def valueAt(subcell: Tuple[int,int,str]) -> str:
            (R, C, ignore) = subcell
            return grid[R][C]

        def external_neighbors(subcell: Tuple[int,int,str]) -> List[Tuple[int,int,str]]:
            # returns a list of either zero or one neighbor, depending on whether
            # the neighbor in this direction is OOB or not.
            (R, C, dir) = subcell
            (I, J) = directions[dir]
            opp = opposites[dir]
            neighbor = (R + I, C + J, opp)
            if legalPos(neighbor):
                return [neighbor]
            else:
                return []

        def internal_neighbors(subcell: Tuple[int,int,str]) -> List[Tuple[int,int,str]]:
            # returns a list of either one or three neighbors, depending on whether
            # there is a space or some sort of slash in the cell
            (R, C, dir) = subcell
            cellType = valueAt(subcell)
            adjacent_sets = adjacent[cellType]
            for S in adjacent_sets:
                if dir in S:
                    return [
                        (R, C, D)
                        for D in S
                        if D != dir
                    ]
            raise Exception(f'ERROR: did not find {dir=} in {adjacent_sets} ("{cellType}")')

        def neighborsOf(subcell: Tuple[int,int,str]) -> List[Tuple[int,int,str]]:
            return external_neighbors(subcell) + internal_neighbors(subcell)

        seen = set()
        regions = 0
        for R in range(grid_R):
            for C in range(grid_C):
                for dir in 'TRBL':
                    subcell = (R, C, dir)
                    # print(f'?: {subcell}')
                    if subcell in seen:
                        # print(f'  (seen)')
                        continue
                    else:
                        seen.add(subcell)
                    regions += 1
                    print(f'NEW REGION #{regions}')
                    queue = {subcell}
                    # paint out this region:
                    while queue:
                        subcell = queue.pop()
                        print(f'  {regions}: {subcell}')
                        for N in neighborsOf(subcell):
                            # print(f'    {N=}')
                            if N in seen:
                                # print(f'      (seen)')
                                continue
                            else:
                                seen.add(N)
                                queue.add(N)
        return regions
# NOTE: Runtime 278 ms Beats 12.25%
# NOTE: Memory 17.23 MB Beats 50.99%
