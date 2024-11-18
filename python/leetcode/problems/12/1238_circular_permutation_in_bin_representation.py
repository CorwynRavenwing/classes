class Solution:

    # This being obviously a Gray Code question,
    # we borrow some code from #89:

    def grayCode(self, n: int) -> List[int]:
        print(f'grayCode({n}):')

        if n == 0:
            return (0,)

        prior = self.grayCode(n - 1)
        print(f'  {prior=}')

        REV = lambda x: tuple(reversed(tuple(x)))

        priorR = REV(prior)
        print(f'  {priorR=}')

        increment = 2 ** (n - 1)
        secondHalf = tuple([
            R + increment
            for R in priorR
        ])
        print(f'{secondHalf=}')

        return prior + secondHalf

    def circularPermutation(self, n: int, start: int) -> List[int]:

        GC = self.grayCode(n)
        index = GC.index(start)

        GC_rotated = GC[index:] + GC[:index]
        return GC_rotated

# NOTE: re-used entire prior version, only adding wrapper code
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 134 ms Beats 28.17%
# NOTE: Memory 25.32 MB Beats 21.13%
