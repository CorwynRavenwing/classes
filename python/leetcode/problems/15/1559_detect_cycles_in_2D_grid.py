class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        grid_M = len(grid)
        grid_N = len(grid[0])
        
        def validPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < grid_M) and (0 <= Y < grid_N)
        
        def OOB(cell: Tuple[int,int]) -> bool:
            return not validPos(cell)
        
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            return [
                (X - 1, Y),
                (X + 1, Y),
                (X, Y - 1),
                (X, Y + 1),
            ]
        
        def valueAt(cell: Tuple[int,int]) -> str:
            nonlocal grid
            if OOB(cell):
                return '?'
            (X, Y) = cell
            return grid[X][Y]

        def validMoves(cell: Tuple[int,int], parent: Tuple[int,int]) -> List[Tuple[int,int]]:
            cellValue = valueAt(cell)
            return [
                N
                for N in neighborsOf(cell)
                if validPos(N)
                if valueAt(N) == cellValue
                if parent is None or parent != N
            ]
            
        seen = set()
        for X in range(grid_M):
            for Y in range(grid_N):
                cell = (X, Y)
                print(f'{cell=}')
                if cell in seen:
                    print(f'  dup')
                    continue
                else:
                    seen.add(cell)
                paths = [(cell,)]
                while paths:
                    print(f'L={len(paths)}')
                    path = paths.pop(0)
                    # if len(path) <= 4:
                    #     print(f'  {path=}')
                    # else:
                    #     print(f'  path={path[:2]} ... {path[-2:]}')
                    if len(path) >= 2:
                        (parent, cell) = path[-2:]  # last 2 cells
                    else:
                        parent = None
                        cell = path[0]
                    print(f'    {parent}:{cell}')
                    seen.add(cell)
                    moves = validMoves(cell, parent)
                    if not moves:
                        print(f'      no moves')
                        continue
                    for M in moves:
                        if M in path:
                            print(f'      LOOP!')
                            return True
                        print(f'      +{M}')
                        paths.append(
                            path + (M,)
                        )
        return False

# NOTE: having timeout errors for large inputs
