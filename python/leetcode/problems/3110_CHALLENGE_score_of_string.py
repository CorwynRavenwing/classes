class Solution:
    def scoreOfString(self, s: str) -> int:

        ans = 0
        ch = s[0]
        prev = ord(ch)
        for ch in s[1:]:
            v = ord(ch)
            ans += abs(prev - v)
            prev = v
        return ans

# NOTE: 27 ms; Beats 96.79% of users with Python3
