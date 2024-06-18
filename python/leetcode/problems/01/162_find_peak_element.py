class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i, N in enumerate(nums):
            # check left side
            prev_N = nums[i - 1] if (i > 0) else None
            next_N = nums[i + 1] if ((i + 1) < len(nums)) else None
            print(f'[{i}]: {prev_N} {N} {next_N}')

            if prev_N is not None and (prev_N >= N):
                print(f'[{i}]:{N} fail left side ({prev_N})')
                continue
            if next_N is not None and (N <= next_N):
                print(f'[{i}]:{N} fail right side ({next_N})')
                continue
            
            return i

