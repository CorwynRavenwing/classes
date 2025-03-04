class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        # step 1: apply the operations
        for i in range(1, len(nums)):
            A = nums[i - 1]
            B = nums[i]
            if A == B:
                nums[i - 1] = A * 2
                nums[i] = 0
            # else do nothing
        print(f'{nums=}')

        # step 2: float 0's to the end:
        zeros = 0
        while 0 in nums:
            zeros += 1
            nums.remove(0)
        print(f'Dropping {zeros=} on the end:')
        nums.extend(
            [0] * zeros
        )

        return nums

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 23 ms Beats 8.25%
# NOTE: Memory 17.90 MB Beats 74.68%
