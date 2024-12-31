class Solution:
    def countGoodStrings(self, minLength: int, maxLength: int, numZeros: int, numOnes: int) -> int:
        
        mod = 10 ** 9 + 7

        @cache
        def DP(length: int) -> int:
            print(f'DP({length})')
            if length > maxLength:
                return 0
            return sum([
                1 if (minLength <= length <= maxLength) else 0,
                DP(length + numZeros),  # DP_pick_0(length)
                DP(length + numOnes),   # DP_pick_1(length)
            ])

        answer = DP(0)

        return answer % mod

# NOTE: usually works, but Memory Limit Exceeded for large inputs
