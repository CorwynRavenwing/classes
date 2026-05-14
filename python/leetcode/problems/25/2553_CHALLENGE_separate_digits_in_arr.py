class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        return [
            int(d)
            for n in nums
            for d in str(n)
        ]
        # NOTE: one-liner

# NOTE: Acceptance Rate 85.7% (easy)

# NOTE: Accepted on second Run (loops in wrong order)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 75.63%
# NOTE: Memory 19.42 MB Beats 47.50%
