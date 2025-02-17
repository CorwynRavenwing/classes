class ProductOfNumbers:

    def __init__(self):
        self.products = []
        return

    def add(self, num: int) -> None:
        self.products.append(1)
        if num == 0:
            self.products = [0] * len(self.products)
        elif num == 1:
            # don't do N multiplications by 1 here
            pass
        else:
            self.products = [
                P * num
                for P in self.products
            ]
        return

    def getProduct(self, k: int) -> int:
        # read from right end of array
        return self.products[-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Time Limit Exceeded)
# NOTE: Runtime 3559 ms Beats 10.22%
# NOTE: Memory 31.49 MB Beats 49.68%

# NOTE: re-ran for challenge:
# NOTE: Runtime 3541 ms Beats 5.18%
# NOTE: Memory 32.32 MB Beats 11.26%
# NOTE: same time and memory; much worse percentages
