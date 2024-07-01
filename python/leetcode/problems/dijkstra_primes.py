class Solution:
    def countPrimes(self, n: int) -> int:

        def prime_iter(primes=None) -> int:
            heap = []
            if primes is None:
                primes = []
            yield 2
            primes.append(2)
            # heap.append(
            #     (2 * 2, 2)
            # )
            stream = itertools.count(3, 2)
            while True:
                N = next(stream)
                # print(f'debug: {N=}')
                # print(f'debug: {heap=}')

                if (not heap) or (N < heap[0][0]):
                    # print(f'  Found new prime {N}')
                    primes.append(N)
                    heap.append(
                        (N * N, N)
                    )
                    yield N
                    continue
                
                # print(f'  {N} not prime:')
                while (heap) and (N == heap[0][0]):
                    heap_obj = heap.pop(0)
                    # print(f'    {N} % {heap_obj[1]}')
                    (M, P) = heap_obj
                    new_obj = (M + P + P, P)
                    bisect.insort(heap, new_obj)
                    # print(f'debug: {heap=}')
                
                assert N < heap[0][0]
        
        primes_found = []
        PI = prime_iter(primes_found)
        
        def isPrime(Q: int) -> bool:
            nonlocal primes_found, PI
            print(f'isPrime({Q}): {primes_found=}')
            # zeroth, 1 is not prime
            if Q == 1:
                print(f'  -> no ({Q} defined as non-prime)')
                return False
            # first, scan the known-primes list
            if Q in primes_found:
                print(f'  -> yes ({Q} known prime)')
                return True
            if Q < max(primes_found, default=0):
                print(f'  -> no ({Q} known non-prime)')
                return False
            for P in primes_found:
                # second, divide by already-known primes
                if Q % P == 0:
                    print(f'  -> no ({Q} non-prime, divisor {P})')
                    return False
                if P * P > Q:
                    print(f'  -> yes ({Q} prime, prime {P}^2 > Q)')
                    return True
            for P in PI:
                # last, divide by newly-produced primes
                if P == Q:
                    print(f'  -> yes ({Q} produced by prime iter)')
                    return True
                if Q % P == 0:
                    print(f'  => no ({Q} non-prime, divisor {P})')
                    return False
                if P * P > Q:
                    print(f'  => yes ({Q} prime, prime {P}^2 > Q)')
                    return True
            assert "prior loop" == "never ends"

        # count_primes = 0
        # for P in prime_iter():
        #     # print(f'  {P} PRIME')
        #     if P >= n:
        #         break
        #     count_primes += 1
        #
        # return count_primes

