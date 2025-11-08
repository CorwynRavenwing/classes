class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        # NOTE: Valid selections are one of the following:
        # (1) zeros, whose prefix sum and suffix sum
        #       are EQUAL, in either direction.
        # (2) zeros whose prefix sum is ONE LESS than
        #       its suffix sum, moving RIGHT only.
        # (3) zeros whose prefix sum is ONE MORE than
        #       its suffix sum, moving LEFT only.
        
        ACC = lambda L: tuple(accumulate(L))
        REV = lambda L: tuple(reversed(L))

        prefix_sum = ACC(nums)
        suffix_sum = REV(ACC(REV(nums)))
        print(f'{nums      =}')
        print(f'{prefix_sum=}')
        print(f'{suffix_sum=}')

        triplets = [
            (A, B)
            for (N, A, B) in zip(nums, prefix_sum, suffix_sum)
            if N == 0
        ]
        print(f'{triplets=}')

        data = [
            (
                2 if (A == B) else
                1 if (A == B - 1) else
                1 if (A == B + 1) else
                0
            )
            for (A, B) in triplets
        ]
        print(f'{data=}')
        
        return sum(data)

# NOTE: Acceptance Rate 56.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 58 ms Beats 29.26%
# NOTE: Memory 17.97 MB Beats 9.04%
