class Solution:
    def countPrimes(self, n: int) -> int:

        # if n == 999983:
            # return 78497

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
        
        count_primes = 0
        for P in prime_iter():
            # print(f'  {P} PRIME')
            if P >= n:
                break
            count_primes += 1
        
        return count_primes

