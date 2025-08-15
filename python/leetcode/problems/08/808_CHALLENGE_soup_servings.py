class Solution:
    def soupServings(self, n: int) -> float:

        # prevent RecursionError exception
        if n > 5000:
            return 1.00000

        average = lambda x: sum(x) / len(x)

        @cache
        def serveMore(A: int, B: int) -> Tuple[float,float]:
            if A < 0: A = 0
            if B < 0: B = 0
            print(f'serveMore({A},{B})')
            if (not A) and (not B):
                return (0,1,0)    # stop: both are zero at once
            elif not A:
                return (1,0,0)    # stop: A is zero and B is not
            elif not B:
                return (0,0,1)    # stop: B is zero and A is not

            answers = (
                serveMore(A - 100, B -  0),
                serveMore(A -  75, B - 25),
                serveMore(A -  50, B - 50),
                serveMore(A -  25, B - 75),
            )
            print(f'  {answers=}')
            inverted = tuple(zip(*answers))
            # print(f'  {inverted=}')
            (A_first_odds, both_odds, B_first_odds) = tuple(map(average, inverted))
            print(f'  (A,both,B)={(A_first_odds, both_odds, B_first_odds)}')
            return (A_first_odds, both_odds, B_first_odds)
        
        (A_first_odds, both_odds, B_first_odds) = serveMore(n, n)
        print(f'ANSWER: (A,both,B)={(A_first_odds, both_odds, B_first_odds)}')

        return A_first_odds + (both_odds / 2)

# NOTE: Acceptance Rate 60.2% (medium)

# NOTE: Accepted on second Submit (first was RecursionError exception)
# NOTE: Runtime 173 ms Beats 20.80%
# NOTE: Memory 21.50 MB Beats 18.55%

# NOTE: re-ran for challenge:
# NOTE: Runtime 139 ms Beats 9.68%
# NOTE: Memory 22.43 MB Beats 9.68%
