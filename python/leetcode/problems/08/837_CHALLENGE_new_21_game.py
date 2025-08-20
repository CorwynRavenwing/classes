class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        # Shortcut for the new version: When we have X points, and
        # we're rolling to see the odds of X+1 .. X+maxPts points,
        # the answer for *each* of those buckets gets incremented
        # by (odds of X points) * (1 / maxPts).  Since we're trying
        # to add a value to every number in a range, we're going to
        # use the PartialSums method, where we start with all values
        # being 0, and in the case above, we add +diff to X and
        # -diff to (X + maxPts + 1): the answer at any point being
        # the sum of all values to its left, inclusive, e.g. [0 .. X]
        #   This reduces the amount of summation we need to do for
        # each point in the loop: instead of needing (maxPts) additions,
        # we instead need only 2.

        Top = min(n, k + maxPts)
        # print(f'DEBUG: {Top=} = min({n}, {k} + {maxPts})')

        Delta = [0] * (n + 2)   # need to store Delta[n + 1]
        Delta[0] += 1.0
        Delta[1] -= 1.0
        current = 0.0
        # print(f'{Delta=}')
        for i in range(0, k):   # k points == stop
            current += Delta[i]
            new_odds = current * (1 / maxPts)
            print(f'{i}={current} ({new_odds}):')
            assert i < k
            j = min(Top, i + maxPts)
            # print(f'j = min({Top}, {i} + {maxPts})')
            # print(f'  DEBUG: updating Delta at [{i+1}] and [{j+1}]')
            Delta[i + 1] += new_odds
            Delta[j + 1] -= new_odds
            # print(f'{Delta=}')

        Odds = tuple(accumulate(Delta))
        print(f'Odds[{k}:{n+1}]={Odds[k:n+1]}')
        return sum(Odds[k:n+1])

# NOTE: Acceptance Rate 45.6% (medium)

# NOTE: A better version than the previous, which minimizes summation
# NOTE: Runtime 457 ms Beats 5.17%
# NOTE: Memory 18.32 MB Beats 5.17%

# NOTE: re-ran for challenge:
# NOTE: Runtime 422 ms Beats 5.16%
# NOTE: Memory 19.27 MB Beats 5.81%
