class Solution:
    def reachNumber(self, target: int) -> int:

        # available = {0}
        # print(f'{available}')
        # for i in itertools.count():
        #     if i > 100:
        #         break
        #     available = {
        #         NEW_A
        #         for A in available
        #         for NEW_A in [A - i, A + i]
        #     }
        #     print(f'{i}: {available}')
        #     if target in available:
        #         return i
        
        # NOTE: this works, but times out for large Target values.

        # the "available" set is always equivalent to:
        # "all even (or odd) numbers from -T to +T
        # where T is the triangle number 1+2+3+...+i"
        # Triangle(X) = (X) * (X + 1) / 2

        # -> (X^2 + something) / 2 = target
        # -> X^2 + something = target * 2
        # -> X^2 = target * 2 - something 
        # -> X < sqrt( target * 2 )

        X = int(sqrt(abs(target) * 2)) - 1
        print(f'{X=}')
        for i in range(X, X + 5):
            triangle = i * (i + 1) // 2
            print(f'  {i=} {triangle=}')
            if triangle < abs(target):
                print(f'    < {target=}')
                continue
            if (triangle % 2) != (target % 2):
                print(f'    Even/Odd disparity ({triangle % 2},{target % 2})')
                continue
            return i
        print(f'Answer not found in range {X}..{X+5}')
        return -999

