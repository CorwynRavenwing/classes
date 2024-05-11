class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        N = 1
        T = ('0' * N) + ('1' * N)
        if T not in s:
            return 0
        
        while T in s:
            print(f"{N=} '{T}' in s: {T in s}")
            N += 1
            T = ('0' * N) + ('1' * N)

        print(f'{N=} {T=} {T in s=}')
        return (N - 1) * 2

