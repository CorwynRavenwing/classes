class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowels = 'aeiou'
        is_vowel = lambda x: (x in vowels)
        all_vowels = set(vowels)

        vowel_counter = Counter()
        consonant_count = 0
        vowel_multiplier = 0

        def has_all_vowels() -> bool:
            nonlocal vowel_counter
            # print(f'{vowel_counter=}')
            nonzero_vowels = +vowel_counter
            # print(f'{nonzero_vowels=}')
            current_vowels = set(nonzero_vowels.keys())
            # print(f'{current_vowels=}')
            return (current_vowels == all_vowels)

        answer = 0

        L = 0
        R = 0
        while L <= R <= len(word):
            try:
                char = word[R]
            except IndexError:
                print(f'*** ran R out of bounds')
                break
            R += 1
            if is_vowel(char):
                vowel_counter[char] += 1
            else:
                consonant_count += 1
            # print(f'[{L},{R}(A)]: "{char}" C={consonant_count}/{k} V={vowel_counter}')
            if consonant_count < k:
                continue
            elif consonant_count > k:
                vowel_multiplier = 0
                while consonant_count > k:
                    try:
                        char = word[L]
                    except IndexError:
                        print(f'*** ran L out of bounds')
                        break
                    L += 1
                    if is_vowel(char):
                        vowel_counter[char] -= 1
                    else:
                        consonant_count -= 1
            assert consonant_count == k
            # print(f'[{L},{R}(B)]: "{char}" C={consonant_count}/{k} V={vowel_counter}')
            if has_all_vowels():
                vowel_multiplier += 1
                answer += vowel_multiplier
                print(f'  {answer=} (+{vowel_multiplier})')

        return answer

# NOTE: Acceptance Rate 40.5% (medium)

# NOTE: had wrong answers: trying another method.

