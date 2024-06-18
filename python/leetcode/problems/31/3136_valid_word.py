class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            print("length < 3")
            return False

        vowels = 'aeiou'
        (count_vowel, count_cons, count_other) = (0, 0, 0)
        for char in word:
            print(f'{char=}')
            char = char.lower()
            if not char.isalnum():
                print(f'character "{char}" not alnum')
                return False
            if char in vowels:
                count_vowel += 1
            elif char.isalpha():
                count_cons += 1
            else:
                count_other += 1
        print(f'{count_vowel=} {count_cons=} {count_other=}')
        if count_vowel == 0:
            print("No vowels")
            return False
        if count_cons == 0:
            print("No consonants")
            return False
        return True

