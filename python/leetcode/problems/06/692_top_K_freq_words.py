class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        counts = Counter(words)
        # can't use most_common(k) because we need to do the
        # sort below *before* the cutoff at k, and most_common()
        # does *not* sort by word, just by count.
        pairs = counts.most_common()
        pairs.sort(
            key=lambda x: (-x[1], x[0])     # by count DESC, then by word ASC
        )
        return [
            word
            for word, count in pairs[:k]
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first found an edge case)
# NOTE: Runtime 67 ms Beats 9.11%
# NOTE: Memory 16.90 MB Beats 7.60%
