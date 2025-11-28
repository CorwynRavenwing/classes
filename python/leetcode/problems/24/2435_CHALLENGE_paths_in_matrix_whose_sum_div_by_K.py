class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        DEBUG = False
        
        mod = 10 ** 9 + 7

        M = len(grid)
        N = len(grid[0])
        if DEBUG: print(f'{M=} {N=}')

        def DP_nocache(x: int, y: int, remainder: int) -> int:
            # nonlocal k
            if DEBUG: print(f'DP([{x},{y}],{remainder})')
            value = grid[x][y]
            if DEBUG: print(f'  ={value}')
            if (x,y) == (0,0):
                answer = (
                    1 if (value % k == remainder)
                    else 0
                )
                if DEBUG: print(f'DP([{x},{y}]: Origin: {answer=}')
                return answer
            if x == 0:
                remainder -= value
                remainder %= k
                answer = DP(x, y-1, remainder)
                if DEBUG: print(f'DP([{x},{y}]: Top Row: {answer=}')
                return answer
            if y == 0:
                remainder -= value
                remainder %= k
                answer = DP(x-1, y, remainder)
                if DEBUG: print(f'DP([{x},{y}]: Left Edge: {answer=}')
                return answer
            else:
                remainder -= value
                remainder %= k
                answer = 0
                answer += DP(x-1, y, remainder)
                answer += DP(x, y-1, remainder)
                # answer %= mod
                if DEBUG: print(f'DP([{x},{y}]: Internal: {answer=}')
                return answer

            assert "we never" == "get here"

        DP_cache = {}
        def DP(x: int, y: int, remainder: int) -> int:
            cache_index = f'({x},{y}):{remainder}'
            if not (cache_index in DP_cache):
                DP_cache[cache_index] = DP_nocache(x, y, remainder)
                
            return DP_cache[cache_index]

        answer = DP(M-1, N-1, 0)

        return answer % mod

# NOTE: Acceptance Rate 46.2% (HARD)

# NOTE: New version with manual cache
# NOTE: Runtime 6465 ms Beats 5.39%
# NOTE: Memory 607.23 MB Beats 8.97%
