class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        nums.append(nums[0])    # circular array: copy first element as new last element
        diffs = [
            abs(A - B)
            for A, B in pairwise(nums)
        ]
        return max(diffs)

# NOTE: Acceptance Rate 70.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.77 MB Beats 48.85%
