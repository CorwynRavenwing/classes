class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        # Shortcut:
        # requirement: "I + R(J) == J + R(I)"
        # this is equivalent to "I - R(I) == J - R(J)"
        # in which each side only contains one variable.
        # so, we compose a list of (X - R[X]) values and look for equal values

        cache = {}
        def R(N: int) -> int:
            if N in cache:
                return cache[N]
            strN = str(N)
            listN = list(strN)
            revListN = reversed(listN)
            revStrN = ''.join(revListN)
            revN = int(revStrN)
            cache[N] = revN
            return revN
        
        def Npick2(N: int) -> int:
            return N * (N - 1) // 2

        NrevN = [
            N - R(N)
            for N in nums
        ]
        print(f'{NrevN=}')

        NrevNcount = Counter(NrevN)
        print(f'{NrevNcount=}')

        answer = 0
        for (number, count) in NrevNcount.items():
            answer += Npick2(count)
        
        mod = 10 ** 9 + 7
        return answer % mod

