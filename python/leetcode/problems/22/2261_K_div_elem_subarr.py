class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        # SHORTCUT 1: we use a sliding window, because
        # we're looking for contiguous groups of elements.
        # For every success, we'll be counting all the
        # possible sub-arrays that *end* with the right-most
        # element in the sliding window.

        # SHORTCUT 2: we pre-process the array, marking the
        # elements that are or are not divisible by p.  Then
        # we get the partial sums of the divisibility array,
        
        nums = tuple(nums)
        divisible = tuple([
            (1 if (N % p == 0) else 0)
            for N in nums
        ])
        # print(f'{divisible=}')

        partialSum = (0,) + tuple(accumulate(divisible))
        # print(f'{partialSum=}')

        L = 0
        R = 1
        answer = set()
        # L,R represent slice [L:R], L-inclusive, R-exclusive.
        while L < R <= len(nums):
            divisible_elements = partialSum[R] - partialSum[L]
            if divisible_elements > k:
                # print(f'[{L}:{R}] no, {divisible_elements} > {k}')
                L += 1
                if L >= R:
                    R += 1
                continue
            # print(f'[{L}:{R}] yes:')
            for M in range(L, R):
                frag = nums[M:R]
                # print(f'  [{M}:{R}] {frag}')
                # if frag in answer:
                #     # print(f'    (seen)')
                # else:
                #     # print(f'    (ADD)')
                answer.add(frag)
            R += 1
        
        # print(f'{answer=}')

        return len(answer)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (var name typo, Output Exceeded)
# NOTE: Runtime 303 ms Beats 62.66%
# NOTE: Memory 32.12 MB Beats 41.94%
