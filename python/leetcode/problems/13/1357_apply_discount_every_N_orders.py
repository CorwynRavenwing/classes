class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer = 0
        self.N = n
        self.NthDiscount = discount
        # self.productPrice = dict(zip(products, prices))
        self.productPrice = {
            product: price
            for product, price in zip(products, prices)
        }
        return

    def getBill(self, products: List[int], amount: List[int]) -> float:
        self.customer += 1
        print(f'Customer #{self.customer}:')

        total = 0
        for (product, quantity) in zip(products, amount):
            priceEach = self.productPrice[product]
            linePrice = priceEach * quantity
            total += linePrice

            print(f'  "{product}":\t{quantity}\t@{priceEach}=\t{linePrice}\t${total}')

        if self.customer % self.N == 0:
            print(f'  {self.NthDiscount}% discount!')
            print(f'  Old {total=}')
            total *= (100 - self.NthDiscount) / 100
            print(f'  New {total=}')

        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

# NOTE: Accepted on second Run (function-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 181 ms Beats 5.10%
# NOTE: Memory 30.06 MB Beats 9.65%
