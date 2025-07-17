class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        
        # from testing: (A) a single banned word appearing
        # in the message twice, DOES count as two banned words
        # (B) a single word, appearing in the banned words list twice,
        # DOES NOT count as two banned words if it appears in the message.

        bannedWords = set(bannedWords)
        spam_points = [
            (
                1 if word in bannedWords
                else 0
            )
            for word in message
        ]
        print(f'{spam_points=}')

        return (sum(spam_points) >= 2)

# NOTE: Acceptance Rate 47.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 83 ms Beats 26.37%
# NOTE: Memory 50.79 MB Beats 93.13%
