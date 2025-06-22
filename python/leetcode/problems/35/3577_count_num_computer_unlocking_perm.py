class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        mod = 10 ** 9 + 7

        # NOTE: if we needed to compute the number of permutations
        # of which computer decrpyted which other computer,
        # this would be a much more complex question.
        # As it stands, however, we only care about the *order*
        # of sequential unlockings.

        complexity_0 = complexity[0]
        for index, C in enumerate(complexity):
            if index == 0:
                continue
            if complexity_0 >= C:
                print(f'FAIL: [0]:{complexity_0} >= [{index}]:{C} ')
                return 0
        
        size = len(complexity) - 1
        
        answer = factorial(size)

        return answer % mod

# NOTE: Acceptance Rate 37.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case requiring modulo)
# NOTE: Runtime 207 ms Beats 24.34%
# NOTE: Memory 32.09 MB Beats 35.09%
