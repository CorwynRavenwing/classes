class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:


        def DP_take(k: int, day: int) -> int:
            price_now = prices[day]
            answers = []
            for future in range(day + 1, len(prices)):
                price_then = prices[future]
                profit = abs(price_then - price_now)
                remainder = DP(k - 1, future + 1)
                answers.append(profit + remainder)
                # print(f'DP_take({k},{day}->{future}) {price_now}-{price_then} + {remainder}')

            return max(answers, default=0)
        
        def DP_skip(k: int, day: int) -> int:
            return DP(k, day + 1)
        
        @cache
        def DP(k: int, day: int) -> int:
            try:
                _ = prices[day]
            except IndexError:
                # last day
                return 0

            if k <= 0:
                # no transactions left
                return 0

            # print(f'DP({k},{day})')

            return max([
                DP_take(k, day),
                DP_skip(k, day),
            ])

        return DP(k, 0)

# NOTE: Acceptance Rate 44.3% (medium)

# NOTE: Time Limit Exceeded for large inputs
