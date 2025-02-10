class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = "aeiou"
        is_vowel = lambda x: (x in vowels)

        word_vowels = [
            (1 if is_vowel(char) else 0)
            for char in word
        ]
        print(f'{word_vowels=}')
        
        L = len(word)
        counts = [
            (count * (index + 1) * (L - index))
            for (index, count) in enumerate(word_vowels)
        ]
        print(f'{counts=}')

        return sum(counts)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 183 ms Beats 5.18%
# NOTE: Memory 25.80 MB Beats 5.93%
