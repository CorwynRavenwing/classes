class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        dictionary.sort(
            key=lambda x: (
                -len(x),    # first, length descending
                x,          # then, lexigraphical order
            )
        )
        # print(f'sorted {dictionary=}')

        def isSubstringOf(needle: str, haystack: str) -> bool:
            # print(f'iSo("{needle}","{haystack}")')
            if not needle:
                return True
            if not haystack:
                return False
            if len(needle) > len(haystack):
                return False
            count_needle = Counter(needle)
            count_haystack = Counter(haystack)
            missing_letters = count_needle - count_haystack
            if missing_letters:
                return False
            
            def found_index_I_after_index_J(i: int, j: int) -> bool:
                # print(f'fIaJ({i},{j})')
                try:
                    char = needle[i]
                except IndexError:
                    # ran out of Needle
                    # print(f'  char="" (success)')
                    return True
                # print(f'  {char=}')
                try:
                    j = haystack.index(char, j)
                except ValueError:
                    # ran out of Haystack
                    # print(f'    j=EOL (failure)')
                    return False
                # print(f'    {j=}')
                return found_index_I_after_index_J(i + 1, j + 1)
            
            return found_index_I_after_index_J(0,0)

        count_S = Counter(s)
        for word in dictionary:
            count_word = Counter(word)
            missing_letters = count_word - count_S
            # print(f'DEBUG: {missing_letters=}')
            if missing_letters:
                continue
            if isSubstringOf(word, s):
                return word

        return ''

# NOTE: Accepted on first Submit
# NOTE: Runtime 216 ms Beats 59.86%
# NOTE: Memory 19.27 MB Beats 6.01%
