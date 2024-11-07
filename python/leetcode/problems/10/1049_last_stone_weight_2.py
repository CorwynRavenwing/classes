class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        # sort and hashable
        stones = tuple(sorted(stones))

        # a single stone can only have one sum.
        # each added stone X can have sums prev_sum +/- X
        # or X +/- prev_sum

        answers = None
        for S in stones:
            if not answers:
                answers = {S}
                print(f'{answers=}')
                continue
            new_answers = {
                N
                for A in answers
                for N in (S-A, A-S, A+S)
            }
            answers = new_answers
            print(f'{answers=}')
        
        possible = {
            A
            for A in answers
            if A >= 0
        }
        print(f'{possible=}')
        return min(possible)

# NOTE: Runtime 15 ms Beats 70.11%
# NOTE: Memory 17.08 MB Beats 45.38%
