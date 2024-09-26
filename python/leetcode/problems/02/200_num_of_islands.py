class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

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
        
        answer = 0
        for X in range(M):
            for Y in range(N):
                cell = (X, Y)
                print(f'{cell=}')
                value = getValue(cell)
                if value != '1':
                    print(f'  No ({value})')
                    continue
                
                answer += 1
                print(f'Found island #{answer} at {cell=}:')
                queue = {cell}
                while queue:
                    cell = queue.pop()
                    print(f'  {cell}')
                    value = getValue(cell)
                    if value != '1':
                        print(f'    (seen)')
                        continue
                    else:
                        setValue(cell, 'X')

                    for C in neighborsOf(cell):
                        value = getValue(C)
                        if value == '1':
                            print(f'    +{C}')
                            queue.add(C)

                print(f'  End of island #{answer}')
        
        print(f'Found a total of {answer} islands.')
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 521 ms Beats 5.03%
# NOTE: Memory 19.17 MB Beats 46.83%
