class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s
# NOTE: Runtime 33 ms Beats 83.28%
# NOTE: Memory 16.52 MB Beats 54.69%

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.98 MB Beats 32.79%
# NOTE: infinitely better runtime
