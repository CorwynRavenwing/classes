class Solution:
    def bulbSwitch(self, n: int) -> int:
        # bulbs = [0] * n
        # # print(f'{0}: {bulbs}')
        # for i in range(1, n+1):
        #     # print(f'{i}:')
        #     for j in range(i, n+1, i):
        #         bulbs[j-1] = 0 if (bulbs[j-1] == 1) else 1
        #         # print(f'  {j}: {bulbs[j-1]}')
        #     # print(f'{i}: {bulbs}')
        # return sum(bulbs)
        # # this question is the equivalent of "count exact squares up to N"
        # # which I replace it with, to fix the timeout issue at testcase 31:
        i = 1
        while (i * i) <= n:
            i += 1
        return (i - 1)

