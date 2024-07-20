class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        return s
# NOTE: Runtime 33 ms Beats 83.28%
# NOTE: Memory 16.52 MB Beats 54.69%
