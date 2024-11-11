class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        Tiring = tuple([
            (1 if work > 8 else 0)
            for work in hours
        ])
        # print(f'{Tiring   =}')
        Nontiring = tuple([
            (0 if T else 1)
            for T in Tiring
        ])
        # print(f'{Nontiring=}')

        ACC = lambda x: (0,) + tuple(accumulate(x))

        sumT = ACC(Tiring)
        sumN = ACC(Nontiring)

        longest = 0
        i = 0
        j = i + 1
        while i < j < len(sumT):
            T = sumT[j] - sumT[i]
            N = sumN[j] - sumN[i]
            W = (T > N)
            L = j - i
            print(f'[{i},{j}]:{L=} {T=} {N=} {W=}')
            if W:
                longest = max(longest, L)
                j += 1
            else:
                i += 1
                if i >= j:
                    j = i + 1

        return longest

# NOTE: was an O(N^2) that worked but was too slow;
#       updated to a sliding-window O(N) that is incorrect.  :-(
