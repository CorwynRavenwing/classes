class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # SHORTCUT: v[i] + v[j] + i - 1
        # === v[i] + i     +      v[j] - j
        # so we can preprocess both of these independently,
        # and add them together later.

        vIplusI = [
            vI + i
            for i, vI in enumerate(values)
        ]
        vJminusJ = [
            vJ - j
            for j, vJ in enumerate(values)
        ]
        print(f'{vIplusI=}')
        print(f'{vJminusJ=}')

        # # this is the right answer, if I can equal J,
        # # which they don't actually forbid in the problem description
        # return max(vIplusI) + max(vJminusJ)
        # # ... but it gives the wrong answer,
        # # so clearly that's not what they wanted.

        # instead, since they only want answers where i < j:
        answers = []
        bestVi = float('-inf')  # guaranteed less than the right answer

        for (Vi, Vj) in zip(vIplusI, vJminusJ):
            # first, add curren Vj to best Vi *to our left*
            answers.append(
                Vj + bestVi
            )
            # second, update bestVi with current Vi value
            bestVi = max(bestVi, Vi)
        
        print(f'{answers=}')
        return max(answers)

# NOTE: Accepted on first Run, with corrected algorithm
# NOTE: Accepted on first Submit
# NOTE: Runtime 96 ms Beats 19.70%
# NOTE: Memory 26.39 MB Beats 5.41%
