class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        low = min(nums)
        high = max(nums)

        present = set(nums)
        missing = [
            X
            for X in range(low, high + 1)
            if X not in present
        ]

        return sorted(missing)

# NOTE: Acceptance Rate 83.4% (easy)

# NOTE: Accepted on second Run (function name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 69.59%
# NOTE: Memory 19.17 MB Beats 86.89%
