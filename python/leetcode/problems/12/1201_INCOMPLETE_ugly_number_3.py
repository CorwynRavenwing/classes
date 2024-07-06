class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        # we borrow some code from #313:

        def generateUgly(primes: List[int]) -> int:

            def prime_generator(prime: int) -> List[int]:
                # print(f'create generator for {prime=}')
                for i in itertools.count(1):
                    yield i * prime

            generators = [
                prime_generator(P)
                for P in primes
            ]

            heap = heapq.merge(*generators)

            prior_ugly = -999
            while True:
                ugly = next(heap)
                if ugly != prior_ugly:
                    prior_ugly = ugly
                    # print(f'found {ugly=}')
                    yield ugly

        uglies = generateUgly([a, b, c])
        for _ in range(1, n):
            skip = next(uglies)
            if skip % 2 != 0:
                print(f'    #{_}: {skip}')
            if _ > 100000000:
                return -99999

        answer = next(uglies)
        print(f'    #{_+1}: {answer} ***')
        return answer

# NOTE: gets Time Limit Exceeded for large inputs.
# Hints suggest using binary search instead of enumerating.
