class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        sorted_words = [
            ''.join(
                sorted(word)
            )
            for word in words
        ]
        # print(f'{sorted_words=}')
        # print(f'{       words=}')

        for i in range(1, len(sorted_words)):
            this_word = sorted_words[i]
            prev_word = sorted_words[i - 1]
            if this_word == prev_word:
                words[i] = None
                # print(f'{       words=}')
        
        answer = [
            word
            for word in words
            if word is not None
        ]

        return answer

# NOTE: Acceptance Rate 60.2% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 3 ms Beats 89.63%
# NOTE: Memory 17.77 MB Beats 76.67%
