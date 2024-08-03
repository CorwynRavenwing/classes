class Solution:
    def countPrimes(self, n: int) -> int:

        def sieve(prime: int, stream: Iterable) -> Iterable:
            return filter(lambda x: x % prime != 0, stream)

        def prime_iter() -> int:
            stream = itertools.count()
            # print(f'debug: {stream=}')
            zeroth = next(stream)
            assert zeroth == 0
            first = next(stream)
            assert first == 1

            while True:
                next_prime = next(stream)
                yield next_prime
                # print(f'adding sieve for prime {next_prime}')
                stream = sieve(next_prime, stream)
                # print(f'debug: {stream=}')

        # if n <= 2:
        #     return 0
        
        count_primes = 0
        for P in prime_iter():
            print(f'  {P} PRIME')
            if P >= n:
                break
            count_primes += 1
        
        return count_primes

