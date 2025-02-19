class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        minMaxIJ_cache = [
            [None] * len(nums)
            for i in range(len(nums))
        ]
        # print(f'{minMaxIJ_cache=}')

        def minMaxIJ_nocache(i: int, j: int) -> Tuple[int,int]:
            # print(f'MM({i},{j})')
            if i > j:
                return (0, 0)
            N = nums[j]
            if i == j:
                return (N, N)
            (prevMin, prevMax) = minMaxIJ(i, j - 1)
            return (
                min(N, prevMin),
                max(N, prevMax),
            )
        
        def minMaxIJ(i: int, j: int) -> Tuple[int,int]:
            cache = minMaxIJ_cache[i][j]
            if cache is None:
                # print(f'  ... compute ({i},{j})')
                cache = minMaxIJ_nocache(i, j)
                minMaxIJ_cache[i][j] = cache
            return cache

        minMaxes = [
            minMaxIJ(i, j)
            for i in range(len(nums))
            for j in range(len(nums))
        ]
        # print(f'{minMaxes=}')

        subtract = lambda x: (x[1] - x[0])

        diffs = map(subtract, minMaxes)

        return sum(diffs)

# NOTE: prior version ran out of time w/o cache and memory w/cache
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit (this version)
# NOTE: Runtime 8031 ms Beats 5.01%
# NOTE: Memory 189.57 MB Beats 11.73%
