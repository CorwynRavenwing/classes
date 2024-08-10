class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = 'aeiou'

        start_and_end_with_vowel = [
            (
                1
                if (word[0] in vowels) and (word[-1] in vowels)
                else 0
            )
            for word in words
        ]
        print(f'{start_and_end_with_vowel=}')
        sums = (0,) + tuple(accumulate(start_and_end_with_vowel))
        print(f'{sums=}')

        return [
            sums[Ri + 1] - sums[Li]
            for Li, Ri in queries
        ]
# NOTE: Runtime 501 ms Beats 84.07%
# NOTE: Memory 57.31 MB Beats 44.07%
