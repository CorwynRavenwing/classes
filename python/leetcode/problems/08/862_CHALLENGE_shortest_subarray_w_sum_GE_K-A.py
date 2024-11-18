class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        if max(nums) >= k:
            return 1
        
        partialSums = (0,) + tuple(accumulate(nums))
        # print(f'{partialSums=}')

        DIFF = lambda T: T[1] - T[0]

        for length in range(2, len(partialSums)):
            print(f'try {length=}')
            diffs = tuple(map(DIFF, zip(partialSums, partialSums[length:])))
            # print(f'  {diffs=}')
            max_diff = max(diffs)
            print(f'  {max_diff=}')
            if max_diff >= k:
                return length
            
        return -1
        
# NOTE: Acceptance Rate 27.0% (HARD)
# NOTE: brute force method.  Times out for large inputs.
