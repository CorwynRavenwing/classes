class Solution:
    def maxDifference(self, s: str) -> int:
        
        counts = Counter(s)
        print(f'{counts=}')
        
        freqs = tuple(counts.values())
        print(f'{freqs=}')

        isEven = lambda x: x % 2 == 0
        isOdd = lambda x: not isEven(x)

        evens = tuple(filter(isEven, freqs))
        odds = tuple(filter(isOdd, freqs))
        print(f'{evens=}')
        print(f'{odds=}')

        return max(odds) - min(evens)

# NOTE: Acceptance Rate 48.9% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 5 ms Beats 21.89%
# NOTE: Memory 18.17 MB Beats 6.41%

# NOTE: re-ran for challenge:
# NOTE: Runtime 11 ms Beats 14.26%
# NOTE: Memory 18.02 MB Beats 6.36%
