class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # INSIGHT: operations "+1" and "*2" imply "binary"

        # SHORTCUT:
        # we add a set bit to a single number with operation 1
        # we move all bits to the left with operation 2
        # therefore the answer is:
        # (A) total set bits in all numbers, plus
        # (B) bit-length minus 1, of largest number

        operation_2s = (
            len(f'{max(nums):b}') - 1
        )

        operation_1s = sum([
            sum(map(int, f'{N:b}'))
            for N in nums
        ])
        print(f'{operation_1s=}')
        print(f'{operation_2s=}')

        return operation_1s + operation_2s

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 283 ms Beats 75.76%
# NOTE: Memory 24.57 MB Beats 43.81%
