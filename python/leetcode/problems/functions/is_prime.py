
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

