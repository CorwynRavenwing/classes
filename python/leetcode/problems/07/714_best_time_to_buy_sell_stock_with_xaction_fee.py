class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # we borrow some code from #122:

        best_values = (0, None)   # (money_without_stock, money_with_stock)
        # print(f'{best_values}')
        for P in prices:
            # print(f'  {P}')
            (old_money_without, old_money_with) = best_values
            (new_money_without, new_money_with) = (0, 0)
            if old_money_with is not None:
                # sell the stock
                new_money_without = old_money_with + P - fee
                # print(f'    try selling stock')
            if old_money_without is not None:
                # buy the stock
                new_money_with = old_money_without - P
                # print(f'    try buying stock')
            best_values = (
                (
                    max(old_money_without, new_money_without)
                    if old_money_without is not None
                    else new_money_without
                ),
                (
                    max(old_money_with, new_money_with)
                    if old_money_with is not None
                    else new_money_with
                ),
            )
            # print(f'{best_values}')
        return max(best_values)

# NOTE: re-used entire previous version, only adding "- fee" update
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 552 ms Beats 53.15%
# NOTE: Memory 23.88 MB Beats 44.95%
