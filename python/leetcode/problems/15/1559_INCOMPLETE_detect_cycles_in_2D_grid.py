class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
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
            (X, Y) = cell
            return grid[X][Y]

        def setValue(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            grid[X][Y] = value
            return True
        
        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]

        seen = set()
        for X in range(M):
            for Y in range(N):
                P = (X, Y)
                if P in seen:
                    print(f'{P}: seen')
                    continue
                else:
                    seen.add(P)
                this_group = {P}
                V = getValue(P)
                print(f'{P}: {V=}')
                state = (P, ())
                queue = {state}
                while queue:
                    state = queue.pop()
                    (P, parent) = state
                    # print(f'  {P} [{parent}]')
                    # print(f'  {P}:')
                    for neighbor in neighborsOf(P):
                        if neighbor == parent:
                            # print(f'    {neighbor} [NO: parent]')
                            continue
                        value = getValue(neighbor)
                        if value != V:
                            # print(f'    {neighbor}: {value} [NO: value]')
                            continue
                        if neighbor in this_group:
                            print(f'    {neighbor} YES: LOOP!')
                            return True
                        # print(f'    -> {neighbor}')
                        state = (neighbor, P)
                        queue.add(state)
        
        print(f'NO: no match')
        return False

# NOTE: Acceptance Rate 53.0% (medium)

# NOTE: Incomplete (Time Limit Exceeded)
