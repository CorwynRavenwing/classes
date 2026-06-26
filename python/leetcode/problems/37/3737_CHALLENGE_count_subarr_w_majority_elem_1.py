class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        points = tuple([
            (
                1 if N == target else -1
            )
            for N in nums
        ])
        print(f'{points=}')

        prefixSum = (0,) + tuple(accumulate(points))
        print(f'{prefixSum=}')

        answers = [
            (L,R,B-A)
            for L, A in enumerate(prefixSum)
            for R, B in enumerate(prefixSum)
            if L < R
            if B-A > 0
        ]
        # print(f'{answers=}')

        return len(answers)

# NOTE: Acceptance Rate 75.5% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2411 ms Beats 17.56%
# NOTE: Memory 85.79 MB Beats 8.56%
