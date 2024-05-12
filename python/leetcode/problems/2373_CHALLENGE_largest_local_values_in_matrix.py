class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def shrink_row(row: List[int]) -> List[int]:
            return list([
                max(row[i-1:i+2])
                for i in range(1, len(row)-1)
            ])
        
        def shrink_grid(grid: List[List[int]]) -> List[List[int]]:
            return list([
                shrink_row(row)
                for row in grid
            ])
            
        print(f'{grid=}')
        shrinkX = shrink_grid(grid)
        print(f'{shrinkX=}')
        shrinkX = list(zip(*shrinkX))
        print(f'reverse {shrinkX=}')
        shrinkY = shrink_grid(shrinkX)
        print(f'{shrinkY=}')
        shrinkY = list(zip(*shrinkY))
        print(f'reverse {shrinkY=}')
        return shrinkY

