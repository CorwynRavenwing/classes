class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def isSubstringOf(needle: str, haystack: str) -> bool:
            print(f'iSo("{needle}","{haystack}")')
            if not needle:
                # remainder of haystack must not contain uppercase chars
                for char in haystack:
                    if char.isupper():
                        print(f'upper {char}')
                        return False
                return True
            if not haystack:
                return False
            if len(needle) > len(haystack):
                return False
            if needle[0] == haystack[0]:
                print(f'match {needle[0]}')
                if isSubstringOf(needle[1:],haystack[1:]):
                    return True
            if haystack[0].isupper():
                print(f'upper {haystack[0]}')
                return False
            return isSubstringOf(needle,haystack[1:])

        def doQuery(Q: List[str]) -> bool:
            print(f'{Q=}')
            return isSubstringOf(pattern, Q)

        return [
            doQuery(Q)
            for Q in queries
        ]

# NOTE: Accepted on first Submit
# NOTE: Runtime 7 ms Beats 9.26%
# NOTE: Memory 16.85 MB Beats 22.45%
