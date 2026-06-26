class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        points = tuple([
            (
                1 if N == target else -1
            )
            for N in nums
        ])
        # print(f'{points=}')

        prefixSum = (0,) + tuple(accumulate(points))
        # print(f'{prefixSum=}')

        answer = 0
        for L, A in enumerate(prefixSum):
            for R in range(L + 1, len(prefixSum)):
                B = prefixSum[R]
                if B - A > 0:
                    answer += 1

        return answer

# NOTE: Acceptance Rate 49.7% (HARD)

# NOTE: incomplete, Time Limit Exceeded even after cleaning up the code
