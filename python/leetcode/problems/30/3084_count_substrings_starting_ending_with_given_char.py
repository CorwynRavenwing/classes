class Solution:
    def countSubstrings(self, s: str, c: str) -> int:

        counts = Counter(s)
        N = counts[c]
        return N * (N+1) // 2   # triangle number 5 + 4 + 3 + 2 + 1

# NOTE: Accepted on first Submit
# NOTE: Runtime 64 ms Beats 16.60%
# NOTE: Memory 17.17 MB Beats 91.32%
