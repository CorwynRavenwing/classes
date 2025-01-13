class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        return sum([
            (1 if W.startswith(pref) else 0)
            for W in words
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 17.99 MB Beats 13.44%
