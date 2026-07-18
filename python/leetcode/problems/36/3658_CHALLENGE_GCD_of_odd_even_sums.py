class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        # Euclidian Algorithm for GCD, as described in Wikipedia
        def GCD(A: int, B: int) -> int:
            # print(f'GCD({A},{B})')
            if B == 0:
                return A
            else:
                return GCD(B, A % B)

        odds = []
        evens = []

        i = 0
        while True:
            i += 1
            if (i % 2) == 0:
                if len(evens) < n:
                    evens.append(i)
                # endif
            else:
                if len(odds) < n:
                    odds.append(i)
                # endif
            if ((len(evens) < n) or (len(odds) < n)):
                continue
            else:
                break 

        print(f'{odds=}')
        print(f'{evens=}')

        sumOdd = sum(odds)
        sumEven = sum(evens)

        print(f'{sumOdd=}')
        print(f'{sumEven=}')

        return GCD(sumOdd, sumEven)

# NONE: Acceptance Rate 88.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 109 ms Beats 6.97%
# NOTE: Memory 19.94 MB Beats 7.06%
