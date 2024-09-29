class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def DP(day: int, haveStock: bool) -> int:
            # print(f'DP({day},{haveStock})')
            if day >= len(prices):
                return 0

            HOLD = DP(
                day + 1,    # come back tomorrow
                haveStock   # changing nothing else
            ) + 0           # and gaining/losing no money
            # print(f'  {HOLD=}')

            if haveStock:
                SELL = DP(
                    day + 2,    # skip cooldown day
                    False       # we no longer have stock we sold
                ) + prices[day] # instead we have $price more money
                # print(f'  {SELL=}')
                return max(SELL, HOLD)
            else:
                BUY = DP(
                    day + 1,    # no cooldown for buying
                    True,       # now we do have a stock
                ) - prices[day] # but we spent $price money
                # print(f'  {BUY =}')
                return max(BUY, HOLD)

        return DP(0, False)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 35 ms Beats 94.81%
# NOTE: Memory 20.68 MB Beats 6.83%
