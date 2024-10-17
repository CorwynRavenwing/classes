class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def isSubstringOf(needle: str, haystack: str) -> bool:
            # print(f'iSo("{needle}","{haystack}")')
            if not needle:
                return True
            if not haystack:
                return False
            if len(needle) > len(haystack):
                return False
            # The following section actually makes it much *slower*:
            # count_needle = Counter(needle)
            # count_haystack = Counter(haystack)
            # missing_letters = count_needle - count_haystack
            # if missing_letters:
            #     return False

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

        return sum([
            count
            for word, count in Counter(words).items()
            if isSubstringOf(word, s)
        ])

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Time Limit Exceeded)
# NOTE: Runtime 285 ms Beats 81.22%
# NOTE: Memory 19.73 MB Beats 31.10%
