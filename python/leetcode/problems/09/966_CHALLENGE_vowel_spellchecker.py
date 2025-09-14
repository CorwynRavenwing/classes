class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def replace_vowels_with_hash(word: str) -> str:
            for vowel in 'aeiou':
                word = word.replace(vowel, '#')
            return word

        exact_match = set(wordlist)
        lower_match = {}
        vowel_match = {}

        for word in wordlist:
            lowercase = word.lower()
            fixvowels = replace_vowels_with_hash(lowercase)
            lower_match.setdefault(lowercase, word)
            vowel_match.setdefault(fixvowels, word)
            # we are using setdefault to pick up only the first such match
        
        print(f'{exact_match=}')
        print(f'{lower_match=}')
        print(f'{vowel_match=}')

        def doQuery(Q: str) -> str:
            if Q in exact_match:
                return Q
            Q = Q.lower()
            if Q in lower_match:
                return lower_match[Q]
            Q = replace_vowels_with_hash(Q)
            if Q in vowel_match:
                return vowel_match[Q]
            return ""

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Acceptance Rate 52.1% (medium)

# NOTE: Accepted on first Submit
# NOTE: Runtime 38 ms Beats 98.42%
# NOTE: Memory 19.19 MB Beats 73.50%

# NOTE: re-ran for challenge:
# NOTE: Runtime 35 ms Beats 81.02%
# NOTE: Memory 20.24 MB Beats 55.81%
