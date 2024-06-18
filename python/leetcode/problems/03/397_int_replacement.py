class Solution:
    def integerReplacement(self, n: int) -> int:

        def show(N: int) -> str:
            return f'{N}={format(N, "b")}'

        steps = 0
        print(f'{steps}: {show(n)}')
        while n > 1:
            steps += 1
            print(f'{steps}: {show(n)}', end=" ")
            if n % 2 == 0:
                n //= 2
                print(f'EVEN -> {show(n)}')
            else:
                binary = format(n, 'b')
                if binary.endswith('01'):
                    n -= 1
                    print(f'01(-) -> {show(n)}')
                elif binary == '11':
                    n -= 1
                    print(f'=11(-) -> {show(n)}')
                elif binary.endswith('11'):
                    n += 1
                    print(f'11(+) -> {show(n)}')
                else:
                    print('ERROR')
                    raise Exception('odd number ends with neither 01 nor 11')
        print(f'{steps}: {show(n)} DONE')
        return steps
# NOTE: a smarter process that knows which path is better at each fork
