class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        # SHORTCUT 1: we don't need to take any F-number more than once.
        # for any four adjacente F-numbers [A, B, C, D],
        # A + B = C   and   B + C = D   by definition.  Therefore:
        # C+C = C + C       # identity
        # C+C = A + B + C   # substitute C=A+B
        # C+C = A + D       # substitute B+C=D
        # So, if we are including number "C" twice in our solution,
        # we can instead include "A" and "D", once each.  If either
        # of those were already in the solution once, we do this
        # process again until we no longer have any duplicates.
        # (For the purpose of this process, F1 = 1 and F2 = 1 do not
        # count as being duplicates.  But if we have a 1 twice,
        # we can always substitute two of them for an F3 = 2 instead.)

        # SHORTCUT 2: we don't need to take any two consecutive F-numbers.
        # If we were taking numbers A and B, we instead take C which equals A+B.

        def fibonacci(limit: int) -> int:
            A = 1
            yield A
            B = 1
            yield B
            while True:
                C = A + B
                if C > limit:
                    return
                yield C
                (A, B) = (B, C)

        fib_gen = fibonacci(k)
        fib_list = list(fib_gen)
        print(f'{fib_list=}')
        count = 0
        while k:
            next_fib = fib_list.pop(-1)
            if next_fib > k:
                continue
            count += 1
            print(f'{count}: {k=} - {next_fib}')
            k -= next_fib
        
        print(f'{count}: {k=}')
        return count

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 10 ms Beats 9.60%
# NOTE: Memory 16.79 MB Beats 11.79%
