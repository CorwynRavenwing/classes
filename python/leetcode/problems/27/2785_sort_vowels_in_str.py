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
# NOTE: Accepted on first Submit
# NOTE: Runtime 112 ms Beats 85.89%
# NOTE: Memory 24.29 MB Beats 9.53%
