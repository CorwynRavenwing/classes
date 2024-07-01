class Solution:
    def primePalindrome(self, n: int) -> int:

        # we're going to want to jump forward
        # to the next palindromic number
        # that does NOT begin/end with
        # a 2, 4, 5, 6, 8, or 0
        # (meaning only 1, 3, 7, 9 are acceptable)
        # and then check for primeness
        #
        # next number after e.g. 234565432
        # is 300000003 (b/c can't start with 2)
        # followed by 300010003 (b/c changing any other number
        # makes a larger "next" value)
        nStr = str(n)
        digits = len(nStr)
        odd = (digits % 2 == 1)
        halfway = (digits // 2) + (digits % 2)     # 4 -> 2; 5 -> 3
        firstHalf = nStr[:halfway]
        root = int(firstHalf)

        def make_palindrome() -> int:
            nonlocal root, odd
            print(f'MP({root},{odd}):')
            rootStr = str(root)
            if odd:
                center = rootStr[-1]
                rootStr = rootStr[:-1]
            else:
                center = ''
                # don't change rootStr
            backHalf = ''.join(
                reversed(rootStr)
            )
            print(f'-> "{rootStr}" + "{center}" + "{backHalf}"')
            answerStr = rootStr + center + backHalf
            return int(answerStr)

        replace_character = {
            '0': '1',   # shouldn't be possible
            '2': '3',
            '4': '7',
            '5': '7',
            '6': '7',
            '8': '9',
        }
        def next_palindrome() -> int:
            nonlocal root, odd
            print(f'NxP({root},{odd}):')
            rootStr = str(root)
            rootLen = len(rootStr)
            root += 1
            rootStr = str(root)
            print(f'  -> {root=} L={rootLen}')
            first = rootStr[0]
            if first in replace_character:
                if (rootLen == 1) and odd:
                    print(f'(ignore first char "{first}" in 1-char number)')
                    pass
                else:
                    print(f'bad first character "{first}":')
                    first = replace_character[first]
                    rest = '0' * (rootLen - 1)
                    rootStr = first + rest
                    print(f'  {digits=}; new number = "{rootStr}"')
                    root = int(rootStr)
            newRootLen = len(rootStr)
            if rootLen != newRootLen:
                rootLen = newRootLen
                odd = (not odd)
                if (not odd):
                    # changing from "odd" to "even" mode:
                    # truncate zero from end of root here
                    rootStr = rootStr[:-1]
                    root = int(rootStr)
                    print(f'    -> {root=} {odd=}')
            return make_palindrome()

        def prime_iter(primes=None) -> int:
            heap = []
            if primes is None:
                primes = []
            primes.append(2)
            # heap.append(
            #     (2 * 2, 2)
            # )
            yield 2
            print(f'PI({primes})')
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
                    print(f'  -> yes ({Q} produced by prime iteratror)')
                    return True
                if Q % P == 0:
                    print(f'  => no ({Q} non-prime, divisor {P})')
                    return False
                if P * P > Q:
                    print(f'  => yes ({Q} prime, prime {P}^2 > Q)')
                    return True
            assert "prior loop" == "never ends"
        
        P = make_palindrome()
        print(f'{P=}')
        while P < n:
            P = next_palindrome()
            print(f'  -> {P=} (was < {n})')
        while not isPrime(P):
            P = next_palindrome()
            print(f'  => {P=} (was not prime)')

        return P

