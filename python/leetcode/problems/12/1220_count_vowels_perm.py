class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # we borrow some code from #935:

        mod = 10 ** 9 + 7

        adjacent = {
            'a': {'e'},
            'e': {'a','i'},
            'i': {'a','e','o','u'},     # == not an 'i'
            'o': {'i','u'},
            'u': {'a'},
        }

        @cache
        def DP(n: int, startFrom=None) -> int:
            if n == 0:
                # print(f'DP({n},{startFrom}): 1')
                return 1
            # print(f'DP({n},{startFrom}):')
            if startFrom is None:
                legalNext = adjacent.keys()
            else:
                legalNext = adjacent[startFrom]
            answers = [
                DP(n - 1, N)
                for N in legalNext
            ]
            answer = sum(answers)
            # print(f'DP({n},{startFrom}): {legalNext}={answers} -> {answer}')
            return answer % mod
        
        answer = DP(n)

        return answer % mod

# NOTE: Acceptance Rate 61.7% (HARD)
# NOTE: Accepted on second Submit (first was Output Exceeds)
# NOTE: Runtime 1582 ms Beats 7.54%
# NOTE: Memory 57.62 MB Beats 34.89%
