class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        L1 = list(map(int, list(num1)))
        L2 = list(map(int, list(num2)))

        print(f'{L1=}')
        print(f'{L2=}')

        partials = [
            (
                [0] * (i)
            ) + [
                (D1 * D2)
                for D2 in L2
            ] + (
                [0] * (len(L1) - i - 1)
            )
            for i, D1 in enumerate(L1)
        ]
        print(f'lengths={list(map(len, partials))}')

        print('partials:')
        for P in partials:
            print(f'  {P}')
        
        product = list(zip(*partials))
        print(f'{product=}')
        product = list(map(sum, product))
        print(f'{product=}')
        while len(product) > 1 and product[0] == 0:
            del product[0]
            print(f'{product=}')
        while max(product) >= 10:
            print(f'{product=}')
            if product[0] >= 10:
                product = [0] + product
                continue
            index = product.index(max(product))
            carry = product[index] // 10
            product[index - 1] += carry
            product[index] -= carry * 10
        print(f'{product=}')
        return ''.join(map(str, product))

