class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        def generateUgly(primes: List[int]) -> int:
            uglies = [1]
            yield 1

            def prime_generator(prime: int) -> List[int]:
                nonlocal uglies
                # print(f'create generator for {prime=}')
                for U in uglies:
                    yield U * prime
            
            generators = [
                prime_generator(P)
                for P in primes
            ]

            heap = heapq.merge(*generators)

            while True:
                ugly = next(heap)
                if ugly != uglies[-1]:
                    uglies.append(ugly)
                    # print(f'found {ugly=}')
                    yield ugly
                # else:
                #     print(f'DUP {ugly=}')
        
        uglies = generateUgly(primes)
        for _ in range(1, n):
            skip = next(uglies)
            # print(f'{_}: {skip}')

        return next(uglies)

# NOTE: 317 ms; Beats 74.18% of users with Python3
