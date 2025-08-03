class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        max_X = max([F[0] for F in fruits] + [startPos])
        # print(f'{max_X=}')

        numberline = [0] * (max_X + 1)
        # print(f'{numberline=}')
        for X, F in fruits:
            numberline[X] = F
        # print(f'{numberline=}')
        
        prefixSum = (0,) + tuple(accumulate(numberline))
        # print(f'{prefixSum=}')

        endpoints = [
            (startPos - left, startPos + k - left - left)
            for left in range(k // 2 + 1)
        ] + [
            (startPos - k + right + right, startPos + right)
            for right in range(k // 2 + 1)
        ]
        # print(f'{endpoints=}')
        endpoints = [
            (
                max(L, 0),
                min(R, max_X)
            )
            for L, R in endpoints
        ]
        # print(f'{endpoints=}')

        scores = [
            prefixSum[R + 1] - prefixSum[L]
            for L, R in endpoints
        ]
        # print(f'{scores=}')

        return max(scores)

# NOTE: Acceptance Rate 38.5% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded masking edge case)
# NOTE: Runtime 1015 ms Beats 16.67%
# NOTE: Memory 85.81 MB Beats 5.00%
