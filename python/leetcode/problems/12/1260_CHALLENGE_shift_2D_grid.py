class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        M = len(grid)
        N = len(grid[0])

        flatten = lambda G: tuple([i for sublist in G for i in sublist])
        unflatten = lambda L: [L[i:i + N] for i in range(0, len(L), N)]
        flat_grid = flatten(grid)
        print(f'{flat_grid=}')
        unflat_grid = unflatten(flat_grid)
        print(f'{unflat_grid=}')
        k %= (M * N)
        print(f'{(M*N)=}; new {k=}')
        # nope, this is rotating backwards
        # rotated_grid = (
        #     flat_grid[k:] + flat_grid[:k]
        # )
        rotated_grid = (
            flat_grid[-k:] + flat_grid[:-k]
        )
        print(f'{rotated_grid=}')
        answer = unflatten(rotated_grid)

        return answer

# NOTE: Acceptance Rate 68.2% (easy)

# NOTE: Accepted on second Run (was rotating backwards)
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 70.58%
# NOTE: Memory 20.00 MB Beats 19.55%
