class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = 'AEIOUaeiou'
        vowel_indexes = []
        vowel_pile = []        # or maybe ... vowel_counts = Counter()
        L = list(s)
        for i, char in enumerate(L):
            if char not in vowels:
                continue
            vowel_indexes.append(i)
            vowel_pile.append(char)
        vowel_pile.sort()
        for i, char in zip(vowel_indexes, vowel_pile):
            L[i] = char

        return ''.join(L)

# NOTE: Acceptance Rate 79.9% (medium)

# NOTE: Accepted on first Submit
# NOTE: Runtime 112 ms Beats 85.89%
# NOTE: Memory 24.29 MB Beats 9.53%

# NOTE: re-ran for challenge:
# NOTE: Runtime 71 ms Beats 84.41%
# NOTE: Memory 24.71 MB Beats 17.75%
