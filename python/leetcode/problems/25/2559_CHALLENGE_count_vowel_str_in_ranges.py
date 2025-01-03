class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        def starts_and_ends_with_vowel(s: str) -> bool:
            
            def is_vowel(s: str) -> bool:
                vowels = 'aeiou'
                return s in vowels
            
            return is_vowel(s[0]) and is_vowel(s[-1])
        
        matching_words = tuple([
            (
                1
                if starts_and_ends_with_vowel(word)
                else 0
            )
            for word in words
        ])
        print(f'{matching_words=}')

        partial_sums = (0,) + tuple(accumulate(matching_words))
        print(f'{partial_sums=}')

        def doQuery(Q: List[int]) -> int:
            print(f'{Q=}')
            (A, B) = Q
            return partial_sums[B + 1] - partial_sums[A]

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 104 ms Beats 6.02%
# NOTE: Memory 51.56 MB Beats 7.31%
