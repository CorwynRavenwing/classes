class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        words = text.split(' ')
        print(f'{words=}')

        broken_letters_in_word = lambda word: [letter for letter in brokenLetters if letter in word]

        word_has_no_broken_letters = lambda word: len(broken_letters_in_word(word)) == 0
        answer = [
            word
            for word in words
            if word_has_no_broken_letters(word)
        ]
        print(f'{answer=}')

        return len(answer)

# NOTE: Acceptance Rate 76.5% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 14.41%
# NOTE: Memory 17.88 MB Beats 57.65%
