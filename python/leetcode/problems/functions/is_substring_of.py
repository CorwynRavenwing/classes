
# Okay, this actually doesn't find "is substring of",
# which is trivially accomplished with "haystack.index(needle)"
# or "needle in haystack"; instead, it finds "is sub*SEQUENCE* of"
# which is much more useful.

# version A:
        def isSubstringOf(needle: str, haystack: str) -> bool:
            if not needle:
                return True
            if not haystack:
                return False
            if len(needle) > len(haystack):
                return False
            if needle[0] == haystack[0]:
                if isSubstringOf(needle[1:],haystack[1:]):
                    return True
            return isSubstringOf(needle,haystack[1:])

# version B:
        def isSubstringOf(needle: str, haystack: str) -> bool:
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
            if needle[0] == haystack[0]:
                if isSubstringOf(needle[1:],haystack[1:]):
                    return True
            return isSubstringOf(needle,haystack[1:])

# version C:
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

