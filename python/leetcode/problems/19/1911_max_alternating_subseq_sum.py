class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        def DP_skip(index, negative: bool) -> int:
            # print(f'  skip({index},{negative})')
            return DP(index + 1, negative)

        def DP_take(index, negative: bool) -> int:
            # print(f'  take({index},{negative})')
            N = nums[index]
            if negative:
                N = -N
            return N + DP(index + 1, not negative)

        @cache
        def DP(index: int, negative=False) -> int:
            # print(f'DP({index},{negative})')
            try:
                check = nums[index]
            except IndexError:
                return 0
            return max([
                DP_skip(index, negative),
                DP_take(index, negative),
            ])
        
        return DP(0)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 1809 ms Beats 13.17%
# NOTE: Memory 378.19 MB Beats 5.40%
