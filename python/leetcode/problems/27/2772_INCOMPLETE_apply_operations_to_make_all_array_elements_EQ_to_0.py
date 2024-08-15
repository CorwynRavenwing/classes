class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:

        i = 0
        while i < len(nums):
            print(f'{nums[i:i+10]}')
            while (i < len(nums)) and (nums[i] == 0):
                # print(f'Skip #0 at [{i}]')
                i += 1
            if i >= len(nums):
                print(f'Overrun: [{i}] >= {len(nums)=}')
                continue
            A = nums[i]
            if A < 0:
                print(f'Underrun: {A=}')
                return False
            print(f'Subtract {A} from [{i}:{i + k}]')
            for j in range(i, i + k):
                if j >= len(nums):
                    print(f'Overrun: [{j}] >= {len(nums)=}')
                    return False
                nums[j] -= A

        print(f'Success!')
        return True
# NOTE: Time Limit Exceeded for large inputs
