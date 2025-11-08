class Solution:

    def grayCode(self, n: int) -> List[int]:
        # print(f'grayCode({n}):')

        if n == 0:
            return (0,)

        prior = self.grayCode(n - 1)
        # print(f'  {prior=}')

        REV = lambda x: tuple(reversed(tuple(x)))

        priorR = REV(prior)
        # print(f'  {priorR=}')

        increment = 2 ** (n - 1)
        secondHalf = tuple([
            R + increment
            for R in priorR
        ])
        # print(f'{secondHalf=}')

        return prior + secondHalf

    def minimumOneBitOperations(self, n: int) -> int:
        print(f'{n=}')
        bin_n = f'{n:b}'
        print(f'{bin_n=}')
        len_n = len(bin_n)
        print(f'{len_n=}')
        gc = self.grayCode(len_n)
        # print(f'{gc=}')
        answer = gc.index(n)
        print(f'{answer=}')
        
        return answer

# NOTE: Acceptance Rate 73.5% (HARD)

# NOTE: Memory Limit Exceeded for large inputs
