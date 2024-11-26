class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        # Every round, pick the two best piles and the worst pile.
        # Alice gets the best, you get the second-best, Bob gets the worst.
        # Poor bob.

        piles.sort()
        one_third = len(piles) // 3
        for_bob = piles[:one_third]     # strip off Bob's set of worst piles
        piles = piles[one_third:]
        piles = tuple(reversed(piles))  # best first
        for_alice = [
            N
            for index, N in enumerate(piles)
            if index % 2 == 0
        ]
        for_me = [
            N
            for index, N in enumerate(piles)
            if index % 2 == 1
        ]
        print(f'{for_alice=}')
        print(f'{for_me   =}')
        print(f'{for_bob  =}')
        return sum(for_me)

# NOTE: Accepted on second Run (variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 120 ms Beats 11.90%
# NOTE: Memory 27.69 MB Beats 42.31%
