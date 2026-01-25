class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        print(f'sorted {nums=}')
        nums_plus_k = nums[k-1:]
        pairs = tuple(zip(nums, nums_plus_k))
        print(f'{pairs=}')
        diffs = [
            (B - A)
            for (A, B) in pairs
        ]
        print(f'{diffs=}')

        return min(diffs)

# NOTE: Acceptance Rate 59.6% (easy)

# NOTE: Accepted on third Run (fencepost error, polarity reversal)
# NOTE: Accepted on first Submit
# NOTE: Runtime 19 ms Beats 9.05%
# NOTE: Memory 19.74 MB Beats 15.85%
