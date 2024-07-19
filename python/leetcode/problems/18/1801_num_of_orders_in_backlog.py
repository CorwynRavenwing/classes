class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy_backlog = []    # each list is [price, quantity]
        sell_backlog = []   # kept in order by price ASC

        for (priceI, amountI, orderTypeI) in orders:
            if orderTypeI == 0:
                # BUY orders
                buy_order = [priceI, amountI]
                print(f'{buy_order=}')
                while buy_order[1]:
                    if not sell_backlog:
                        break
                    lowest_price_sell = sell_backlog[0]   # bottom end == low price
                    transaction_size = min(buy_order[1], lowest_price_sell[1])
                    transaction_price = lowest_price_sell[0]
                    if transaction_price <= priceI:
                        print(f'  sell {transaction_size} at {transaction_price}')
                        buy_order[1] -= transaction_size
                        lowest_price_sell[1] -= transaction_size
                        if lowest_price_sell[1] == 0:
                            print(f'    (sell order consumed)')
                            del sell_backlog[0]     # again, low end
                    else:
                        print(f'  price too low: {transaction_price} > {priceI}')
                        break
                if buy_order[1]:
                    print(f'  buy order not completely executed')
                    bisect.insort(buy_backlog, buy_order)
            elif orderTypeI == 1:
                # SELL orders
                sell_order = [priceI, amountI]
                print(f'{sell_order=}')
                while sell_order[1]:
                    if not buy_backlog:
                        break
                    highest_price_buy = buy_backlog[-1]   # top end == high price
                    transaction_size = min(sell_order[1], highest_price_buy[1])
                    transaction_price = highest_price_buy[0]
                    if transaction_price >= priceI:
                        print(f'  buy {transaction_size} at {transaction_price}')
                        sell_order[1] -= transaction_size
                        highest_price_buy[1] -= transaction_size
                        if highest_price_buy[1] == 0:
                            print(f'    (buy order consumed)')
                            del buy_backlog[-1]     # again, high end
                    else:
                        print(f'  price too low: {transaction_price} > {priceI}')
                        break
                if sell_order[1]:
                    print(f'  sell order not completely executed')
                    bisect.insort(sell_backlog, sell_order)
            else:
                raise Exception(f'ERROR: {orderTypeI=} must be either 0 or 1')
        
        def count_backlog(BL: List[Tuple[int,int]]) -> int:
            answer = 0
            for (price, quantity) in BL:
                answer += quantity
            return answer
        
        mod = 10 ** 9 + 7

        return (count_backlog(buy_backlog) + count_backlog(sell_backlog)) % mod

