class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowels = 'aeiou'
        is_vowel = lambda x: (x in vowels)
        all_vowels = set(vowels)

        def countSubstringsAtLeastK(k: int) -> int:
            print(f'C_S_GE_K({k}):')

            vowel_counter = Counter()
            consonant_count = 0

            def has_all_vowels() -> bool:
                nonlocal vowel_counter
                nonzero_vowels = +vowel_counter
                current_vowels = set(nonzero_vowels.keys())
                return (current_vowels == all_vowels)
            
            missing_any_vowels = lambda: (not has_all_vowels())

            # SHOW = lambda COUNT: ''.join(sorted(set((+COUNT).keys())))

            answer = 0

            L = 0
            R = 0

            while L <= R <= len(word):
                if (consonant_count < k) or missing_any_vowels():
                    # print(f'(bump R right)')
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
                    # print(f'[{L},{R}]: "{char}" C={consonant_count}/{k} V={SHOW(vowel_counter)}')
                    continue
                delta = len(word) - R + 1
                answer += delta
                # print(f'  {answer=} (+{delta})')
                # print(f'(bump L right)')
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

            return answer

        at_least_k = countSubstringsAtLeastK(k)
        at_least_k_plus_1 = countSubstringsAtLeastK(k + 1)
        exactly_k = at_least_k - at_least_k_plus_1

        print(f'{exactly_k=} = {at_least_k=} - {at_least_k_plus_1=}')

        return exactly_k

# NOTE: Acceptance Rate 40.5% (medium)

# NOTE: Time Limit Exceeded: trying another method
