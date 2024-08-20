class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        for i in range(len(nums) - indexDifference):
            A = nums[i]
            # print(f'{i=} {A=}')
            for j in range(i + indexDifference, len(nums)):
                B = nums[j]
                diff = abs(A - B)
                # print(f'  {j=} {B=} {diff=}')
                if diff >= valueDifference:
                    return [i, j]
        
        return [-1, -1]

# NOTE: brute force: works, but Time Limit Exceeded for large inputs
