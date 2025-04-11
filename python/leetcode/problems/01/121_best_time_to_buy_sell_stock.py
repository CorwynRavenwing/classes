<pre>class Solution:
    def maxProfit(self, prices: List[int]) -&gt; int:
        
        min_buy_price = prices[0]
        max_profit = 0

        for price in prices:
            if price &lt; min_buy_price:
                min_buy_price = price
            else:
                profit = price - min_buy_price
                if profit &gt; max_profit:
                    max_profit = profit
        
        return max_profit

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 26 ms Beats 91.21%
# NOTE: Memory 26.93 MB Beats 33.24%</pre>