class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return 0
        nums.sort()
        answer = None
        prior = nums.pop(0)
        for N in nums:
            gap = N - prior
            prior = N
            if answer is None or answer < gap:
                answer = gap
                print(f'{prior=} {N=} {gap=}')
        return answer

# NOTE: 727 ms; Beats 86.45% of users with Python3
