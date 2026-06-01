class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse=True)
        print(f'{cost=}')

        prices = [
            price
            for index, price in enumerate(cost)
            if index % 3 != 2
        ]
        print(f'{prices=}')

        return sum(prices)

# NOTE: Acceptance Rate 63.8% (easy)

# NOTE: Accepted on second Run (one-character variable name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 19.30 MB Beats 48.06%
