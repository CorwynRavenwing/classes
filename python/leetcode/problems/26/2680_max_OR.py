class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:

        bitwise_or = lambda x, y: x | y
        REV = lambda x: tuple(reversed(tuple(x)))
        SHIFT_ADD_ZERO = lambda x: ((0,) + tuple(x)[:-1])
        # PARTIAL_OR = lambda x: ((0,) + tuple(accumulate(x, bitwise_or))[:-1])
        PARTIAL_OR = lambda x: SHIFT_ADD_ZERO(accumulate(x, bitwise_or))
        # PARTIAL_OR = lambda x: tuple(accumulate(x, bitwise_or))

        nums.sort()
        # print(f'sorted {nums=}')
        partialOrLeft = PARTIAL_OR(nums)
        # print(f'{partialOrLeft=}')
        partialOrRight = REV(PARTIAL_OR(REV(nums)))
        # print(f'{partialOrRight=}')

        answer = 0
        for i, N in enumerate(nums):
            left_Or = partialOrLeft[i]
            right_Or = partialOrRight[i]
            # print(f'{i}: [{left_Or}] {N=} [{right_Or}]')
            N <<= k         # left shift number by K bits
            # print(f'  shifted: {N=}')
            total_Or = left_Or | N | right_Or
            # print(f'  {total_Or=}')

            answer = max(answer, total_Or)

        return answer
# NOTE: Runtime 685 ms Beats 23.31%
# NOTE: Memory 31.26 MB Beats 33.08%
