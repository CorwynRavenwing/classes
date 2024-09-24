class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        words_by_first_char = {}
        for word in dictionary:
            firstChar = word[0]
            words_by_first_char.setdefault(firstChar, set())
            words_by_first_char[firstChar].add(word)
        print(f'{words_by_first_char=}')

        @cache
        def DP(s: str) -> int:
            print(f'DP({s}):')
            nonlocal words_by_first_char
            if not s:
                print(f'  null string')
                return 0
            firstChar = s[0]
            remainder = s[1:]
            answer_skipping_first_char = 1 + DP(remainder)
            if firstChar not in words_by_first_char:
                print(f'  skip first char "{firstChar}"')
                return answer_skipping_first_char
            wordList = words_by_first_char[firstChar]
            print(f'  {len(wordList)} matches for first char "{firstChar}"')
            answers = [
                DP(s[len(word):])
                for word in wordList
                if s.startswith(word)
            ] + [
                answer_skipping_first_char
            ]
            print(f'  {answers=}')
            return min(answers)
        
        return DP(s)

# NOTE: Accepted on first Submit
# NOTE: Runtime 218 ms Beats 42.21%
# NOTE: Memory 17.16 MB Beats 35.55%
