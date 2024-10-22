class Solution:
    def knightDialer(self, n: int) -> int:

        mod = 10 ** 9 + 7

        adjacent = {
            0: {4,6},
            1: {6,8},
            2: {7,9},
            3: {4,8},
            4: {0,3,9},
            5: {},
            6: {0,1,7},
            7: {2,6},
            8: {1,3},
            9: {2,4},
        }

        @cache
        def DP(n: int, startFrom=None) -> int:
            # print(f'DP({n},{startFrom})')
            if n == 0:
                return 1
            if startFrom is None:
                legalNext = adjacent.keys()
            else:
                legalNext = adjacent[startFrom]
            answer = sum([
                DP(n - 1, N)
                for N in legalNext
            ])
            return answer % mod
        
        answer = DP(n)

        return answer % mod

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 2162 ms Beats 17.66%
# NOTE: Memory 41.38 MB Beats 24.74%
