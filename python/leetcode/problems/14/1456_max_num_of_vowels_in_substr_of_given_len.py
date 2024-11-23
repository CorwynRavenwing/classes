class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        VOWEL = lambda char: char in 'aeiou'

        I = 0
        vowels = 0
        for J in range(I, k):
            if VOWEL(s[J]):
                vowels += 1
            # print(f'{I=} {J=} {s[I]=} {s[J]=} {vowels=} -')
        J += 1
        
        max_vowels = vowels
        while 0 <= I < J <= len(s):
            max_vowels = max(vowels, max_vowels)
            # try:
            #     print(f'{I=} {J=} {s[I]=} {s[J]=} {vowels=} {max_vowels=}')
            # except IndexError:
            #     break
            if max_vowels == k:
                break
            try:
                if VOWEL(s[I]):
                    vowels -= 1
                if VOWEL(s[J]):
                    vowels += 1
            except IndexError:
                break
            I += 1
            J += 1
        
        return max_vowels

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (was Output Exceeded)
# NOTE: Runtime 114 ms Beats 25.91%
# NOTE: Memory 16.96 MB Beats 98.60%
