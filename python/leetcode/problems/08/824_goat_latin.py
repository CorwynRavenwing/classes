class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        def begins_with_vowel(s: str) -> bool:
            vowels = 'AEIOUaeiou'
            first = s[0]
            return first in vowels
        
        words = sentence.split(' ')
        goat = []
        for word in words:
            print(f"  {word}", end=" -> ")
            if not begins_with_vowel(word):
                # move first letter to end
                word = word[1:] + word[:1]
            word += "ma"
            word += "a" * (len(goat) + 1)
            print(f"{word}")
            goat.append(word)
        return ' '.join(goat)

