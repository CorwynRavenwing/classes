class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        grid_M = len(grid)
        grid_N = len(grid[0])

        @cache
        def rhombus_pattern(size: int) -> Set[Tuple[int,int]]:
            print(f'Computing rhombus_pattern({size})')
            answer = set()
            for i in range(size + 1):
                j = size - i
                answer.add((+i, +j))
                answer.add((+i, -j))
                answer.add((-i, +j))
                answer.add((-i, -j))
            return answer
        
        def legalCell(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < grid_M) and (0 <= Y < grid_N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalCell(cell)

        def rhombus_cells(center: Tuple[int,int], size: int) -> Set[Tuple[int,int]]:
            (X, Y) = center
            answer = {
                (X + I, Y + J)
                for (I, J) in rhombus_pattern(size)
            }
            bad_cells = [
                cell
                for cell in answer
                if OOB(cell)
            ]
            if bad_cells:
                print(f'rc({center},{size}) OOB: {list(sorted(bad_cells))}')
                return None
            return answer

        def valueAt(cell: Tuple[int,int]) -> int:
            nonlocal grid
            if OOB(cell):
                raise Exception(f'ERROR: {cell=} is OOB!')
            (X, Y) = cell
            return grid[X][Y]
        
        def sumOfCells(cells: Set[Tuple[int,int]]) -> int:
            return sum([
                valueAt(cell)
                for cell in cells
            ])
        
        def rhombus_sum(center: Tuple[int,int], size: int) -> int:
            return sumOfCells(
                rhombus_cells(center, size)
            )
        
        flatten = (
            cell
            for row in grid
            for cell in row
        )
        top3 = sorted(set(flatten), reverse=True)[:3]
        print(f'with size 0 rhombi: {top3=}')
        
        max_size = min(grid_M, grid_N) // 2
        for size in range(1, max_size + 1):
            for X in range(size, grid_M - size):
                for Y in range(size, grid_N - size):
                    center = (X, Y)
                    top3.append(rhombus_sum(center, size))
            top3 = sorted(set(top3), reverse=True)[:3]
            print(f'with {size=} rhombi: {top3=}')

        return top3

