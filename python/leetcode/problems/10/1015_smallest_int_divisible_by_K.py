class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        N = 0
        Nstr = ''
        for length in range(1, k + 1):
            N *= 10
            N += 1
            Nstr += '1'
            mod = N % k
            # print(f'{length=} N={Nstr} {mod=}')
            if mod == 0:
                return length
        return -1

