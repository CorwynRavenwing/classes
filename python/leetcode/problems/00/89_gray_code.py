class Solution:
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

# NOTE: Accepted on first Submit
# NOTE: Runtime 83 ms Beats 30.22%
# NOTE: Memory 24.01 MB Beats 44.82%
