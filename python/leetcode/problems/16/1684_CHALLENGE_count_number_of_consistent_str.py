class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        inconsistentLetters = [
            [
                letter
                for letter in word
                if letter not in allowed
            ]
            for word in words
        ]
        print(f'{inconsistentLetters=}')

        inconsistentCount = tuple(map(len, inconsistentLetters))
        print(f'{inconsistentCount=}')

        consistentWords = [
            index
            # words[index]
            for index, count in enumerate(inconsistentCount)
            if count == 0
        ]
        print(f'{consistentWords=}')

        return len(consistentWords)

# NOTE: Accepted on first Submit
# NOTE: Runtime 249 ms Beats 9.60%
# NOTE: Memory 19.71 MB Beats 5.72%
