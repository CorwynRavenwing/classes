class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        profits = [
            P * S
            for P, S in zip(prices, strategy)
        ]
        print(f'{profits=}')

        ACC = lambda L: (0,) + tuple(accumulate(L))

        partialProfits = ACC(profits)   # profit if we perform "strategy"
        print(f'{partialProfits=}')

        partialSell = ACC(prices)       # profit if we always sell
        print(f'{partialSell=}')

        answers = []
        for L in range(len(prices)):
            M = L + k // 2
            R = L + k
            # add the following:
            # partialProfits from 0 to L
            # zero fom L to M
            # partialSell from M to R
            # partialProfits from R to end
            # add this sum to answers
        
        return max(answers, default=0)

# NOTE: Acceptance Rate 50.9% (medium)

# NOTE: incompete.  pseudocode written: turn into a program.
