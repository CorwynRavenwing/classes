class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        mod = 12345

        grid = [
            [
                value % mod
                for value in row
            ]
            for row in grid
        ]

        # we borrow some code from #238:

        operator_mul_mod = lambda x, y: (x * y) % mod
        MUL = lambda x: (1,) + tuple(accumulate(x, operator_mul_mod))
        REV = lambda x: tuple(reversed(tuple(x)))

        def productExceptSelf(nums: List[int]) -> List[int]:

            partialProductLeft = MUL(nums)
            partialProductRight = REV(MUL(REV(nums)))

            # print(f'{partialProductLeft=}')
            # print(f'{partialProductRight=}')

            return [
                partialProductLeft[i] * partialProductRight[i + 1]
                for i in range(len(nums))
            ]

        rowProducts = [
            math.prod(row)
            for row in grid
        ]
        # print(f'{rowProducts=}')

        PES_multipliers = productExceptSelf(rowProducts)
        # print(f'{PES_multipliers=}')

        PES_per_row = [
            productExceptSelf(row)
            for row in grid
        ]
        # print(f'{PES_per_row=}')

        answer = [
            [
                (PES_mult * value) % mod
                for value in row_PES
            ]
            for PES_mult, row_PES in zip(PES_multipliers, PES_per_row)
        ]
        # print(f'{answer=}')
        return answer

# NOTE: Runtime 1358 ms Beats 13.34%
# NOTE: Memory 72.38 MB Beats 6.67%
