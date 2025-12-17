class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        NEGINF = float('-inf')
        LONG = +1
        SHORT = -1
        EVEN = 0
        
        # parameters per hint by rxndosiel:
        # owned === stocks you currently own: -1 (short), +1 (long), 0 (neither)
        def DP_take(k: int, owned: int, day: int) -> int:
            price = prices[day]
            if owned == LONG:
                # sell it
                return -price + DP(k, EVEN, day + 1)
                
            if owned == SHORT:
                # buy it back
                return +price + DP(k, EVEN, day + 1)

            if owned == EVEN:
                # free to buy or sell
                return max([
                    -price + DP(k - 1, LONG, day + 1),     # buy
                    +price + DP(k - 1, SHORT, day + 1),    # sell
                ])

        def DP_skip(k: int, owned: int, day: int) -> int:
            return DP(k, owned, day + 1)

        def DP(k: int, owned: int, day: int) -> int:
            try:
                _ = prices[day]
            except IndexError:
                # last day
                if owned != EVEN:
                    # haven't closed our transaction
                    return NEGINF
                else:
                    return 0

            if k <= 0:
                # no transactions left
                return 0

            print(f'DP({k},{owned},{day})')

            return max([
                DP_take(k, owned, day),
                DP_skip(k, owned, day),
            ])
        
        return DP(k, EVEN, 0)

# NOTE: Acceptance Rate 44.3% (medium)

# NOTE: wrong answer
