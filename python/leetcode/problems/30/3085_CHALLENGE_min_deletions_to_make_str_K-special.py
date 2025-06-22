class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        counts = Counter(word)
        print(f'{counts=}')
        freq = set(counts.values())
        print(f'{freq=}')

        answers = [
            [
                (
                    y
                    if y < x else
                    y - x - k
                    if y > x + k else
                    0
                )
                for (item, y) in counts.items()
            ]
            for x in freq
        ]
        print(f'{answers=}')
        answers = tuple(map(sum, answers))
        print(f'{answers=}')

        return min(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 106 ms Beats 40.72%
# NOTE: Memory 17.75 MB Beats 17.01%

# NOTE: re-ran for challenge:
# NOTE: Runtime 57 ms Beats 68.99%
# NOTE: Memory 18.47 MB Beats 4.65%
