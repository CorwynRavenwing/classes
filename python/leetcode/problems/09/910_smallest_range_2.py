class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            return 0
        
        nums.sort()
        plus = [N + k for N in nums]
        minus = [N - k for N in nums]
        MIN = plus[0]
        MAX = minus[-1]
        SCORE = plus[-1] - MIN

        if k == 0:
            return SCORE
        
        for i in range(1, len(nums)):
            mx = max(MAX, plus[i - 1])
            mn = min(MIN, minus[i])
            score = mx - mn
            print(f'{i=} {mn}:{mx} -> {score=}')
            if SCORE > score:
                print(f'  NEW MINIMUM!')
                SCORE = score
        
        return SCORE

