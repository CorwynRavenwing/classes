class StockSpanner:

    def __init__(self):
        self.Data = []
        print(f'DEBUG: init {self.Data}')
        return

    def next(self, price: int) -> int:
        print(f'next({price})')
        span = 1
        while self.Data:
            (old_price, old_span) = self.Data[-1]
            if old_price <= price:
                span += old_span
                del self.Data[-1]
                print(f'DEBUG: del: {self.Data}')
            else:
                break
        new_data = (price, span)
        self.Data.append(new_data)
        print(f'DEBUG: add: {self.Data}')
        print(f'  -> {span}')
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (small logic error in edge case)
# NOTE: Runtime 400 ms Beats 7.57%
# NOTE: Memory 21.61 MB Beats 45.02%
