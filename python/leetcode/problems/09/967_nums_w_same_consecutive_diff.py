class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        # we borrow some code from #935:

        DistanceKFrom = lambda X: {
            N
            for N in (X - k, X + k)
            if 0 <= N <= 9
        }

        adjacent = {
            N: DistanceKFrom(N)
            for N in range(0, 9+1)
        }
        print(f'{adjacent=}')

        @cache
        def DP(n: int, startFrom=None) -> int:
            print(f'DP({n},{startFrom})')
            if n == 0:
                return ['']
            if startFrom is None:
                legalNext = set(adjacent.keys()) - {0}
            else:
                legalNext = adjacent[startFrom]

            answer = []
            for N in legalNext:
                for A in DP(n - 1, N):
                    answer.append(str(N) + A)

            print(f'DP({n},{startFrom}): {answer}')
            return answer

        answer = DP(n)

        return tuple(map(int, answer))

# NOTE: Accepted on first Submit
# NOTE: Runtime 6 ms Beats 98.19%
# NOTE: Memory 17.85 MB Beats 6.32%
