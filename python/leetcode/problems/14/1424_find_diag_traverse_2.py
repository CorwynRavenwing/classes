class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        # we borrow some code from #498:

        # having noticed that each diagonal is full of cells
        # where their (X + Y) is the same for that diagonal,

        diags = {}
        for X, row in enumerate(nums):
            for Y, value in enumerate(row):
                D = X + Y
                diags.setdefault(D, [])
                diags[D].append(value)
        print(f'{diags=}')
        # This gives us each diagonal in *UR->LL direction* order.
        # to get *LL->UR direction* order, we reverse all the rows.

        REV = lambda x: tuple(reversed(tuple(x)))
        diagsInOrder = [
            REV(diagonal)
            for rowNum, diagonal in sorted(diags.items())
        ]
        print(f'{diagsInOrder=}')

        return [
            D
            for flatten in diagsInOrder
            for D in flatten
        ]

# NOTE: re-used all the prior version's code, with tiny changes
# NOTE: Accepted on first Submit
# NOTE: Runtime 845 ms Beats 5.32%
# NOTE: Memory 50.93 MB Beats 5.06%
