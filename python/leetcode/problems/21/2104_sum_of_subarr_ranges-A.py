class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        @cache
        def minMaxIJ(i: int, j: int) -> Tuple[int,int]:
            # print(f'MM({i},{j})')
            if i > j:
                return (0, 0)    # minMaxIJ(j, i)
            N = nums[j]
            if i == j:
                return (N, N)
            (prevMin, prevMax) = minMaxIJ(i, j - 1)
            return (
                min(N, prevMin),
                max(N, prevMax),
            )
        
        minMaxes = [
            minMaxIJ(i, j)
            for i in range(len(nums))
            for j in range(len(nums))
        ]
        # print(f'{minMaxes=}')

        subtract = lambda x: (x[1] - x[0])

        diffs = map(subtract, minMaxes)

        return sum(diffs)

# NOTE: without cache: Time Limit Exceeded
# NOTE: with cache: Memory Limit Exceeded
