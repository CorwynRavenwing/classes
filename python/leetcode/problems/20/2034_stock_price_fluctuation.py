class StockPrice:

    def __init__(self):
        self.stockPriceAtTime = {}
        self.maxTimestamp = -1
        self.maxPrice = None
        self.minPrice = None

    def update(self, timestamp: int, price: int) -> None:
        # print(f'update({timestamp},{price}):')
        if timestamp in self.stockPriceAtTime:
            oldprice = self.stockPriceAtTime[timestamp]
            if self.minPrice == oldprice:
                # print(f'  Invalidate old min {oldprice}')
                self.minPrice = None
            if self.maxPrice == oldprice:
                # print(f'  Invalidate old max {oldprice}')
                self.maxPrice = None
        #     print(f'  Overwrite {oldprice} with {price}')
        # else:
        #     print(f'  New price {price}')
        self.stockPriceAtTime[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)
        # update min/max if invalidated earlier:
        if self.minPrice is None:
            self.minPrice = self.minimum()
        if self.maxPrice is None:
            self.maxPrice = self.maximum()
        # set min/max from this value
        if self.minPrice is None or self.minPrice > price:
            # print(f'  New min = {price}')
            self.minPrice = price
        if self.maxPrice is None or self.maxPrice < price:
            # print(f'  New max = {price}')
            self.maxPrice = price
        return

    def current(self) -> int:
        timestamp = self.maxTimestamp
        answer = self.stockPriceAtTime[timestamp]
        # print(f'current(): {timestamp=} {answer=}')
        return answer

    def allCurrentPrices(self) -> List[int]:
        return self.stockPriceAtTime.values()
        
    def maximum(self) -> int:
        if self.maxPrice is None:
            # print(f'maximum(): recreate max price')
            self.maxPrice = max(self.allCurrentPrices())
        # print(f'maximum(): {self.maxPrice}')
        return self.maxPrice

    def minimum(self) -> int:
        if self.minPrice is None:
            # print(f'minimum(): recreate min price')
            self.minPrice = min(self.allCurrentPrices())
        # print(f'minimum(): {self.minPrice}')
        return self.minPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
