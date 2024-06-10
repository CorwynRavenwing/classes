class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        diffs = [
            (1 if (A != B) else 0)
            for (A, B) in zip(heights, expected)
        ]
        return sum(diffs)

