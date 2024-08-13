class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        COMMA = ','
        for D in '0123456789':
            D2 = D+D
            if D2 in s:
                while D2 in s:
                    s = s.replace(D2, D+COMMA+D)     # e.g. "33" -> "3,3"
                print(f'{D=} {s=}')
        groups = s.split(COMMA)
        print(f'{groups=}')
        lengths = tuple(map(len, groups))
        print(f'{lengths=}')
        if len(lengths) == 1:
            return lengths[0]

        pairs = tuple(pairwise(lengths))
        print(f'{pairs=}')
        sums = tuple(map(sum, pairs))
        print(f'{sums=}')

        return max(sums)
# NOTE: Runtime 93 ms Beats 7.89%
# NOTE: Memory 17.02 MB Beats 7.53%
