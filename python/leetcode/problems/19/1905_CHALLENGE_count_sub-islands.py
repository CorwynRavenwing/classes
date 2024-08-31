class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        landOn1 = {
            (X, Y)
            for X, row in enumerate(grid1)
            for Y, val in enumerate(row)
            if val == 1
        }
        landOn2 = {
            (X, Y)
            for X, row in enumerate(grid2)
            for Y, val in enumerate(row)
            if val == 1
        }
        # print(f'{landOn1=}')
        # print(f'{landOn2=}')

        grid_X = len(grid1)
        grid_Y = len(grid1[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < grid_X) and (0 <= Y < grid_Y)
        
        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)
        
        directions = {
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        }

        # def value1(cell: Tuple[int,int]) -> int:
        #     if legalPos(cell):
        #         return 0
        #     (X, Y) = cell
        #     return grid1[X][Y]

        def value2(cell: Tuple[int,int]) -> int:
            if OOB(cell):
                return 0
            (X, Y) = cell
            return grid2[X][Y]

        def rawNeighbors(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            return [
                (X + I, Y + J)
                for (I, J) in directions
            ]

        def neighbors2(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            return [
                N
                for N in rawNeighbors(cell) # neighboring cell
                if value2(N) == 1           # must be land
            ]
        
        seen = set()
        groups = []
        for C in landOn2:
            # print(f'{C=}')
            if C in seen:
                # print(f'  (seen)')
                continue
            else:
                seen.add(C)
            # print(f'  NEW GROUP')
            thisGroup = {C}
            queue = {C}
            while queue:
                Q = queue.pop()
                # print(f'  {Q=}')
                for N in neighbors2(Q):
                    # print(f'    {N=}')
                    if N in seen:
                        # print(f'      (seen)')
                        continue
                    else:
                        seen.add(N)
                    queue.add(N)
                    thisGroup.add(N)
            # print(f'{thisGroup=}')
            groups.append(thisGroup)
            thisGroup = None
        # print(f'{groups=}')
        subgroupDetails = [
            [
                cell in landOn1
                for cell in group
            ]
            for group in groups
        ]
        # print(f'{subgroupDetails=}')
        subgroups = [
            1 if all(D) else 0
            for D in subgroupDetails
        ]
        print(f'{subgroups=}')
        
        return sum(subgroups)

# NOTE: Runtime 3259 ms Beats 5.04%
# NOTE: Memory 83.31 MB Beats 5.04%
