class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        def bin2int(row: List[int]) -> int:
            answer = 0
            for bit in row:
                answer *= 2
                answer += bit
            return answer
        
        def score_grid(grid: List[List[int]]) -> int:
            scores = [
                bin2int(row)
                for row in grid
            ]
            return sum(scores)
        
        def flip_row(row: List[int]) -> List[int]:
            new_row = [
                (
                    0
                    if bit == 1
                    else
                    1
                )
                for bit in row
            ]
            return list(new_row)

        def grid_flip_row(grid: List[List[int]], rowId: int) -> List[List[int]]:
            new_row = flip_row(grid[rowId])
            new_grid = [
                (
                    new_row
                    if i == rowId
                    else row
                )
                for i, row in enumerate(grid)
            ]
            return list(new_grid)
        
        def grid_flip_column(grid: List[List[int]], colId: int) -> List[List[int]]:
            zip_grid = list(zip(*grid))
            zip_answer = grid_flip_row(zip_grid, colId)
            answer = list(zip(*zip_answer))
            return answer

        def show_grid(label: str, score: int, grid: List[List[int]]) -> None:
            show_rows = [
                ' '.join(map(str, row))
                for row in grid
            ]
            print(f'# *** {label} ({score=}) *** #')
            print('\n'.join(show_rows))
            pass
        
        best_score = score_grid(grid)
        show_grid('begin', best_score, grid)

        for i in range(len(grid)):
            grid_i = grid_flip_row(grid, i)
            new_score = score_grid(grid_i)
            if new_score > best_score:
                show_grid(f'swap {i=}', new_score, grid_i)
                best_score = new_score
                grid = grid_i
            else:
                print(f'swapping {i=} made it worse ({new_score=})')
        
        for j in range(len(grid[0])):
            grid_j = grid_flip_column(grid, j)
            new_score = score_grid(grid_j)
            if new_score > best_score:
                show_grid(f'swap {j=}', new_score, grid_j)
                best_score = new_score
                grid = grid_j
            else:
                print(f'swapping {j=} made it worse ({new_score=})')

        return best_score

