class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        return [
            index
            for index, word in enumerate(words)
            if x in word
        ]

# NOTE: one-line answer (wrapped for clarity)
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 32.18%
# NOTE: Memory 17.89 MB Beats 40.28%
