class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        
        INF = float('+inf')    # guaranteed NOT to be the minimum

        OP1 = lambda X: ((X + 1) // 2)
        OP2 = lambda X: ((X - k) if (X >= k) else X)

        def DP_skip(index: int, op1: int, op2: int) -> int:
            value = nums[index]
            recurse = DP(index + 1, op1, op2)
            return value + recurse

        def DP_op1(index: int, op1: int, op2: int) -> int:
            if (op1 < 1):
                return INF
            value = OP1(nums[index])
            recurse = DP(index + 1, op1 - 1, op2)
            return value + recurse

        def DP_op2(index: int, op1: int, op2: int) -> int:
            if (op2 < 1):
                return INF
            value = OP2(nums[index])
            recurse = DP(index + 1, op1, op2 - 1)
            return value + recurse

        def DP_op1_op2(index: int, op1: int, op2: int) -> int:
            if (op1 < 1) or (op2 < 1):
                return INF
            # note that these are in the opposite order:
            value = OP1(OP2(nums[index]))
            recurse = DP(index + 1, op1 - 1, op2 - 1)
            return value + recurse

        def DP_op2_op1(index: int, op1: int, op2: int) -> int:
            if (op1 < 1) or (op2 < 1):
                return INF
            # note that these are in the opposite order:
            value = OP2(OP1(nums[index]))
            recurse = DP(index + 1, op1 - 1, op2 - 1)
            return value + recurse

        @cache
        def DP(index: int, op1: int, op2: int) -> int:
            try:
                value = nums[index]
            except IndexError:
                return 0    # ran out of nums: sum === 0
            return min([
                DP_skip(index, op1, op2),
                DP_op1(index, op1, op2),
                DP_op2(index, op1, op2),
                DP_op1_op2(index, op1, op2),
                DP_op2_op1(index, op1, op2),
            ])
        
        answer = DP(0, op1, op2)

        if answer == INF:
            return -1
        
        return answer

# NOTE: Acceptance Rate 29.7% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded: added cache)
# NOTE: Runtime 6158 ms Beats 5.60%
# NOTE: Memory 370.32 MB Beats 5.60%
