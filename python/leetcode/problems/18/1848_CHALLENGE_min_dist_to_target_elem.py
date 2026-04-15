class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        answers = [
            abs(start - index)
            for index, value in enumerate(nums)
            if value == target
        ]
        print(f'{answers=}')
        return min(answers)

# NOTE: Acceptance Rate 54.4% (easy)

# NOTE: Accepted on second Run (function name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.52 MB Beats 24.63%
