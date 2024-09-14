class Solution:
    def stringHash(self, s: str, k: int) -> str:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        HASH = lambda x: alphabet.index(x)
        UNHASH = lambda x: alphabet[x]
        SUM_MOD_26 = lambda x: (sum(x) % 26)
        JOIN = lambda x: ''.join(x)

        substrings = []
        while s:
            SS = s[:k]
            s = s[k:]
            substrings.append(SS)
        print(f'{substrings=}')

        answer = JOIN([
            UNHASH(
                SUM_MOD_26(
                    map(HASH, SS)
                )
            )
            for SS in substrings
        ])

        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 80 ms Beats 5.31%
# NOTE: Memory 16.84 MB Beats 27.05%
