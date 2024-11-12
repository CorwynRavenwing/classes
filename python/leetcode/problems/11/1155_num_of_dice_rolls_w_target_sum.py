class Solution:

    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 0:
            # out of dice
            if target == 0:
                # on target
                print(f'NR2T({n},{k},{target}): YES')
                return 1
            else:
                # not on target
                print(f'NR2T({n},{k},{target}): NO')
                return 0
        
        # all dice, all sizes is too low: impossible
        if n * k < target:
            print(f'NR2T({n},{k},{target}): low')
            return 0
        # exact match
        if n * k < target:
            print(f'NR2T({n},{k},{target}): ALL {k}s')
            return 1
        
        # all dice, all ones is too high: impossible
        if n * 1 > target:
            print(f'NR2T({n},{k},{target}): high')
            return 0
        # exact match
        if n * 1 > target:
            print(f'NR2T({n},{k},{target}): ALL {1}s')
            return 1

        print(f'NR2T({n},{k},{target}): ?')
        answers = [
            self.numRollsToTarget(
                n - 1,
                k,
                target - roll
            )
            for roll in range(1, k + 1)
        ]
        # print(f'NR2T({n},{k},{target}): {answers=}')
        answer = sum(answers) % MOD
        print(f'NR2T({n},{k},{target}): {answer=}')

        return answer

# NOTE: Accepted on second Run (first was modulo 10^9+7)
# NOTE: Accepted on first Submit
# NOTE: Runtime 87 ms Beats 92.85%
# NOTE: Memory 20.96 MB Beats 38.59%
