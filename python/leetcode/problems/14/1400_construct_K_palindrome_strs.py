class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counts = Counter(s)
        print(f'{counts=}')
        odd_counts = sum([
            0 if (count % 2 == 0) else 1
            for (letter, count) in counts.items()
        ])
        print(f'{odd_counts=}')
        return (odd_counts <= k)

# NOTE: Accepted on second Run (first was variable-name typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 27 ms Beats 91.57%
# NOTE: Memory 17.23 MB Beats 54.18%
