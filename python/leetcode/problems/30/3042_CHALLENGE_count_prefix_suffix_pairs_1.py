class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if len(str1) > len(str2):
                # print(f'  NO (len >) "{str1}" "{str2}"')
                return False
            if not str2.startswith(str1):
                # print(f'  NO (start) "{str1}" "{str2}"')
                return False
            if not str2.endswith(str1):
                # print(f'  NO (end)   "{str1}" "{str2}"')
                return False
            # print(f'  YES        "{str1}" "{str2}"')
            return True

        # don't sort, because we actually care about i < j
        answer = 0
        for i, str1 in enumerate(words):
            for j, str2 in enumerate(words):
                if i >= j:
                    # print(f'SKIP ({i}>={j}) "{str1}" "{str2}"')
                    continue
                if isPrefixAndSuffix(str1, str2):
                    print(f'MATCH "{str1}" "{str2}"')
                    answer += 1

        return answer

# NOTE: Accepted on second Submit (edge case with identical strings)
# NOTE: Runtime 19 ms Beats 11.25%
# NOTE: Memory 17.64 MB Beats 34.51%
