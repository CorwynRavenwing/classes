class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mins = [None] * len(nums)
        maxs = [None] * len(nums)
        mins[0] = nums[0]
        maxs[-1] = nums[-1]
        # print(f'{mins=}')
        # print(f'{nums=}')
        # print(f'{maxs=}')
        for i, N in enumerate(nums):
            # print(f'[{i}]:{N} {mins[i]}')
            if mins[i] is not None:
                continue
            mins[i] = min(nums[i], mins[i-1])
        for i, N in reversed(list(enumerate(nums))):
            # print(f'[{i}]:{N} {maxs[i]}')
            if maxs[i] is not None:
                continue
            maxs[i] = max(nums[i], maxs[i+1])
        print(f'{mins=}')
        print(f'{nums=}')
        print(f'{maxs=}')
        for i, N in enumerate(nums):
            if mins[i] < N < maxs[i]:
                print(f'match {mins[i]} {N} {maxs[i]}')
                return True
        print(f'no match')
        return False

