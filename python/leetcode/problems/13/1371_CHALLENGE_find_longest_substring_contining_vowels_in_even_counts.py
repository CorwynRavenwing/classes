class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = 'aeiou'
        codes = [
            (
                2 ** vowels.index(C)
                if C in vowels
                else 0
            )
            for C in s
        ]
        # print(f'{codes=}')
        codes_XOR = (0,) + tuple(accumulate(codes, operator.xor))
        # print(f'{codes_XOR=}')
        XOR_indexes = {}
        for i, X in enumerate(codes_XOR):
            XOR_indexes.setdefault(X, [])
            XOR_indexes[X].append(i)
        # print(f'{XOR_indexes=}')
        index_dist = [
            indexes[-1] - indexes[0]
            for XOR, indexes in XOR_indexes.items()
        ]
        print(f'{index_dist=}')
        return max(index_dist)

# NOTE: Runtime 301 ms Beats 58.22%
# NOTE: Memory 49.65 MB Beats 5.01%
