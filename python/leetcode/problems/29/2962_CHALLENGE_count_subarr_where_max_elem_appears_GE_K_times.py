class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        max_elem = max(nums)
        is_max = [
            (1 if (N == max_elem) else 0)
            for N in nums
        ]
        # print(f'{is_max=}')
        partialSum = (0,) + tuple(accumulate(is_max))
        # print(f'{partialSum=}')
        len_sums = len(partialSum)

        answer = 0

        for L, left in enumerate(partialSum):
            # print(f'[{L}]:{left} -> ')
            right = left + k
            R = bisect_left(partialSum, right, L)
            additional = len_sums - R
            # print(f'  [{R}]:{right} +{additional}')
            answer += additional

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 300 ms Beats 5.10%
# NOTE: Memory 30.50 MB Beats 7.04%
