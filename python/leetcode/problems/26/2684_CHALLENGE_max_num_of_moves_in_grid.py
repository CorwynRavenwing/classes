class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        # first I'm going to swap rows and columns so we can
        # move downward by rows instead of crosswise by columns:

        grid = tuple(zip(*grid))
        # print(f'{grid=}')
        allowed = {i for i in range(len(grid[0]))}
        # print(f'  {allowed=}')
        for moves in range(1, len(grid)):
            print(f'{moves=}')
            newAllowed = set()
            for A in allowed:
                N = grid[moves-1][A]
                print(f'  i={A} prior={N}')
                for B in [A-1, A, A+1]:
                    if (B < 0) or (B >= len(grid[0])):
                        # print(f'    skip {B}')
                        continue
                    P = grid[moves][B]
                    if N >= P:
                        # print(f'    too small {P}')
                        continue
                    else:
                        print(f'    allow {P}')
                        newAllowed.add(B)
            allowed = newAllowed
            print(f'  {allowed=}')
            if len(allowed) == 0:
                print(f'    Stuck.  Return {moves - 1}')
                return moves - 1
        
        print(f'Finished!  Return {moves}')
        return moves
# NOTE: Runtime 1078 ms Beats 47.98%
# NOTE: Memory 26.66 MB Beats 98.48%

# NOTE: ran again for challenge:
# NOTE: Runtime 230 ms Beats 42.42%
# NOTE: Memory 26.64 MB Beats 96.82%
