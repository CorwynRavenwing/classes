class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        @cache
        def isprime(N: int) -> bool:
            trivial_primes = [2, 3, 5, 7]
            if N in trivial_primes:
                print(f'{N=} trivial prime')
                return True
            if N < 10:
                print(f'{N=} trivial non-prime')
                return False
            for P in trivial_primes:
                if N % P == 0:
                    print(f'{N=} non-prime {P=}')
                    return False
            k = 5
            # all primes > 3 will be of the form 6x-1 or 6x+1:
            # therefore check only those
            while k * k <= N:
                print(f'{N=} Check {k} and {k+2}')
                if N % k == 0:
                    print(f'{N=} non-prime {k=}')
                    return False
                if N % (k + 2) == 0:
                    print(f'{N=} non-prime {k+2=}')
                    return False
                k += 6
            print(f'{N=} prime ({k=} {k*k=})')
            return True

        # print(f'TEST: {isprime(11)=}')

        primes = [
            N if isprime(N) else ''
            for N in nums
        ]
        print(f'{primes=}')

        indexes = [
            index
            for index, P in enumerate(primes)
            if P
        ]
        print(f'{indexes=}')

        return max(indexes) - min(indexes)

# NOTE: Accepted on first Submit
# NOTE: Runtime 814 ms Beats 44.74%
# NOTE: Memory 28.58 MB Beats 5.26%
