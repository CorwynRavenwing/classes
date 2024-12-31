class Solution:
    def countGoodStrings(self, minLength: int, maxLength: int, numZeros: int, numOnes: int) -> int:
        
        mod = 10 ** 9 + 7
        
        answers = [1] + [0] * (maxLength)

        for i, A in enumerate(answers):
            if A == 0:
                print(f'[{i}]{A}:')
                print(f'  Zero')
                continue
            # print(f'[{i}]{A}:')
            for j in [i + numZeros, i + numOnes]:
                if j > maxLength:
                    print(f'[{i}]{A}:')
                    print(f'  [{j}] OOB')
                    continue
                # print(f'  [{j}]')
                answers[j] += A
                answers[j] %= mod
                # print(f'  -> {answers[j]}')
        # print(f'{answers=}')

        partialSums = tuple(accumulate(answers))
        # print(f'{partialSums=}')

        answer = partialSums[maxLength] - partialSums[minLength - 1]

        return answer % mod

# NOTE: new version without recursion
# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 323 ms Beats 28.50%
# NOTE: Memory 27.99 MB Beats 64.72%
