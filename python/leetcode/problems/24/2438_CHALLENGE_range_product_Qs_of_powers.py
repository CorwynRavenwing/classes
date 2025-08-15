class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        mod = 10 ** 9 + 7

        binary = f'{n:b}'
        print(f'{n=} {binary=}')
        # powers = tuple([
        #     2 ** i
        #     for i, D in enumerate(reversed(binary))
        #     if D == '1'
        # ])
        # print(f'{powers=}')
        exponents = tuple([
            i
            for i, D in enumerate(reversed(binary))
            if D == '1'
        ])
        print(f'{exponents=}')

        @cache
        def doQuery(Q: List[int]) -> int:
            (leftI, rightI) = Q
            # brute force is okay here, as our maximum length is 32 here
            expList = exponents[leftI:rightI + 1]
            # product of powers === sum of exponents
            exponent = sum(expList)
            answer = 2 ** exponent
            print(f'{Q=}: {expList=} {exponent=} {answer=}')
            return answer % mod
        
        return [
            doQuery(tuple(Q))
            for Q in queries
        ]

# NOTE: Acceptance Rate 48.5% (medium)

# NOTE: Runtime 1395 ms Beats 60.23%
# NOTE: Memory 52.15 MB Beats 92.40%

# NOTE: re-ran for challenge:
# NOTE: Runtime 36 ms Beats 85.09%
# NOTE: Memory 45.06 MB Beats 93.17%
