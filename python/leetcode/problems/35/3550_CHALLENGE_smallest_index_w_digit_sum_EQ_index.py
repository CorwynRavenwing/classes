class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for idx, N in enumerate(nums):
            digits = tuple(
                map(
                    int,
                    str(N)
                )
            )
            digit_sum = sum(digits)
            print(f'{idx}: {N} {digit_sum}={digits}')
            if idx == digit_sum:
                return idx
        
        print(f'nope')
        return -1

# NOTE: Acceptance Rate 79.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 15 ms Beats 16.46%
# NOTE: Memory 19.33 MB Beats 29.46%
