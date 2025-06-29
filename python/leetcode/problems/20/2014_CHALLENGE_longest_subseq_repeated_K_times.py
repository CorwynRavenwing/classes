class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:

        # returns all possible strings in reverse alpha order
        def all_strings_length_L(L: int, freq: Dict[str,int]) -> List[str]:
            if L == 0:
                yield ''
                return
            
            available_letters = [
                letter
                for letter, count in freq.items()
                if count > 0
            ]
            available_letters.sort(reverse=True)
            for first in available_letters:
                remaining_freq = {
                    letter: (
                        count - 1
                        if letter == first
                        else count 
                    )
                    for letter, count in freq.items()
                }
                print(f'  {first}: {remaining_freq}')
                for others in all_strings_length_L(L - 1, remaining_freq):
                    yield first + others
            return
        
# version A:
        def isSubstringOf_A(needle: str, haystack: str) -> bool:
            if not needle:
                return True
            if not haystack:
                return False
            if len(needle) > len(haystack):
                return False
            if needle[0] == haystack[0]:
                if isSubstringOf_A(needle[1:],haystack[1:]):
                    return True
            return isSubstringOf_A(needle,haystack[1:])

# version B:
        def isSubstringOf_B(needle: str, haystack: str) -> bool:
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
                if isSubstringOf_B(needle[1:],haystack[1:]):
                    return True
            return isSubstringOf_B(needle,haystack[1:])

# version C:
        def isSubstringOf_C(needle: str, haystack: str) -> bool:
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
        
        # isSubstringOf = isSubstringOf_A     # A: TLE @63
        # isSubstringOf = isSubstringOf_B     # B: TLE @119
        isSubstringOf = isSubstringOf_C     # C: works!

        n = len(s)
        longest_possible_sequence = n // k
        print(f'{n=} longest={longest_possible_sequence}')

        count_all = Counter(s)
        # print(f'  {count_all=}')
        frequencies = {
            letter: count // k
            for letter, count in count_all.items()
            if (count // k)
        }
        print(f'  {frequencies=}')

        for length in reversed(range(longest_possible_sequence + 1)):
            print(f'\nTry {length=}')
            for string in all_strings_length_L(length, frequencies):
                attempt = string * k
                if isSubstringOf(attempt, s):
                    return string
        return ""

# NOTE: Acceptance Rate 55.0% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Time Limit Exceeded, twice)
# NOTE: Runtime 3317 ms Beats 21.13%
# NOTE: Memory 19.03 MB Beats 22.54%
