class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        def div_ceil(numerator: int, denominator: int) -> int:
            # returns ceil(numerator / denominator)
            return sum([
                numerator // denominator,
                # this returns N // D   if the division is exact,
                # or (N // D) + 1       if N/D has a remainder.
                0 if (numerator % denominator == 0) else 1,
            ])
        
        nums.sort()
        score = 0
        # print(f'DEBUG: {nums=}')
        for _ in range(k):
            # always choose the highest value
            N = nums.pop(-1)
            score += N
            new_N = div_ceil(N, 3)
            # print(f'{_+1}/{k}: {score=} {N} -> {new_N}')
            bisect.insort(nums, new_N)
            # print(f'DEBUG: {nums=}')
        
        return score
# NOTE: Runtime 4382 ms Beats 5.32%
# NOTE: Memory 31.14 MB Beats 65.96%
