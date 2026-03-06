class Solution:
    def minOperations(self, s: str) -> int:
        
        pairs = tuple(enumerate(s))
        print(f'{pairs=}')

        data = [
            (I + int(N)) % 2
            for (I, N) in pairs
        ]
        print(f'{data=}')

        counts = Counter(data)
        counts[0] += 0
        counts[1] += 0
        print(f'{counts=}')

        answers = counts.values()
        print(f'{answers=}')

        return min(answers)

# NOTE: Acceptance Rate 67.0% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 43 ms Beats 5.33%
# NOTE: Memory 20.76 MB Beats 7.69%
