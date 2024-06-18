class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        mods = [None] * len(nums)
        mods[0] = nums[0] % k
        for i in range(1, len(nums)):
            mods[i] = (mods[i-1] + nums[i]) % k
        # mods = [
        #     sum(nums[:i+1]) % k
        #     for i in range(len(nums))
        # ]
        if mods[0] == 0:
            mods[0] = 'X'
        for i in reversed(range(1, len(nums))):
            if mods[i-1] == mods[i]:
                mods[i-1] = 'X'
        if 0 in mods:
            # having deleted off the 0th column zero,
            # any other zero means we can add columns 0 .. n for a win
            return True
        while 'X' in mods:
            mods.remove('X')
        print(f'{mods=}')
        counts = Counter(mods)
        print(f'{counts=}')
        for number, count in counts.items():
            if count > 1:
                return True
        return False

