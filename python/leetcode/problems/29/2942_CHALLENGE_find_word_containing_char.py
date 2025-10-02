class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        return [
            index
            for index, word in enumerate(words)
            if x in word
        ]

# NOTE: Acceptance Rate 90.5% (easy)

# NOTE: one-line answer (wrapped for clarity)
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 32.18%
# NOTE: Memory 17.89 MB Beats 40.28%

# NOTE: re-ran for challenge:
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 18.02 MB Beats 23.44%
