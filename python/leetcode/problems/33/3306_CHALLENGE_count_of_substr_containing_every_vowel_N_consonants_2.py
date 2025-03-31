class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        vowels = 'aeiou'
        is_vowel = lambda x: x in vowels
        is_consonant = lambda x: not is_vowel(x)
        all_vowels = set(vowels)
        CONSONANT = "Z"
        letterCount = Counter()
        used_vowels = lambda: set(letterCount.keys()) - {CONSONANT}
        has_all_vowels = lambda: used_vowels() == all_vowels

        word = ''.join([
            (
                char
                if is_vowel(char)
                else CONSONANT
            )
            for char in word
        ])
        # print(f'{word=}')

        nextConsonant = [None] * len(word)
        nextConsonantIndex = len(word)

        for i in reversed(range(len(word))):
            nextConsonant[i] = nextConsonantIndex
            if is_consonant(word[i]):
                nextConsonantIndex = i
                
        # print(f'{nextConsonant=}')

        answer = 0
        L = 0
        R = 0

        while L <= R < len(word):
            char = word[R]
            letterCount[char] += 1
            # print(f'[{L}:{R}] "{char}"')
            while letterCount[CONSONANT] > k:
                # print(f'  C>{k}: shrink')
                char = word[L]
                letterCount[char] -= 1
                if not letterCount[char]:
                    del letterCount[char]
                L += 1
                # print(f'  [{L}:{R}] "{char}"')
            
            while (
                L < len(word)
                and letterCount[CONSONANT] == k
                and has_all_vowels()
            ):
                change = nextConsonant[R] - R
                answer += change
                # print(f'  OK: record {change=} ({answer=}) and shrink')
                char = word[L]
                letterCount[char] -= 1
                if not letterCount[char]:
                    del letterCount[char]
                L += 1
                # print(f'  [{L}:{R}] "{char}"')
            
            R += 1
        
        return answer

# NOTE: Acceptance Rate 40.5% (medium)

# NOTE: Runtime 4345 ms Beats 6.94%
# NOTE: Memory 25.43 MB Beats 11.06%
