class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

# Version 1:
        start = 0
        for s0 in s:
            # print(f"{s0=}")
            pos = t.find(s0, start)
            # print(f"  {start=} {pos=}")
            if pos == -1:
                # print(f"    FAIL {pos=}")
                return False
            start = pos + 1
        return True

# Version 2:

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

        return isSubstringOf(s, t)

# NOTE: Version 1:
# NOTE: Runtime 38 ms Beats 40.95%
# NOTE: Memory 16.68 MB Beats 29.85%

# NOTE: Version 2:
# NOTE: Runtime 36 ms Beats 52.89%
# NOTE: Memory 16.76 MB Beats 6.78%
