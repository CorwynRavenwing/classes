class Solution:
    def minDeletion(self, nums: List[int]) -> int:

        deletes_past = 0
        i = 0
        while i <= len(nums) - 2:
            (A, B) = nums[i:i+2]
            # print(f'{i}: {A},{B}')
            if A != B:
                # print(f'  Different = OK!')
                i += 2  # skip both numbers
            else:
                # print(f'  Same = delete either one')
                deletes_past += 1
                i += 1  # skip deleted number

        print(f'Remainder: {nums[i:i+2]}; {i=} {len(nums)=}')
        if i == len(nums) - 1:
            print(f'  One left == odd number: delete last one')
            return deletes_past + 1
        else:
            return deletes_past
# NOTE: Runtime 968 ms Beats 37.31%
# NOTE: O(N)
# NOTE: Memory 30.57 MB Beats 91.04%
# NOTE: O(1)
