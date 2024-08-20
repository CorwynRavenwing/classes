class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # operator.mul = lambda x, y: x * y
        MUL = lambda x: (1,) + tuple(accumulate(x, operator.mul))
        REV = lambda x: tuple(reversed(tuple(x)))

        partialProductLeft = MUL(nums)
        partialProductRight = REV(MUL(REV(nums)))

        print(f'{partialProductLeft=}')
        print(f'{partialProductRight=}')

        return [
            partialProductLeft[i] * partialProductRight[i + 1]
            for i in range(len(nums))
        ]

# NOTE: Accepted on first Submit
# NOTE: Runtime 286 ms Beats 15.71%
# NOTE: Memory 26.49 MB Beats 8.08%
