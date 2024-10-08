class Solution:
    def minLength(self, s: str) -> int:

        prior = s + 'guaranteed not to match'
        print(f'{s=}')
        while prior != s:
            prior = s
            s = s.replace('AB', '')
            print(f'{s=}')
            s = s.replace('CD', '')
            print(f'{s=}')
        return len(s)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 44 ms Beats 57.39%
# NOTE: Memory 16.76 MB Beats 7.81%
