from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = Counter(s)
        # print(f"{letters=}")
        answer = 0
        singleton = 0
        for letter, count in letters.items():
            # print(f"  '{letter}': {count}")
            if count % 2 != 0:
                singleton = 1
            answer += (count // 2) * 2
        if singleton:
            answer += 1
        return answer

