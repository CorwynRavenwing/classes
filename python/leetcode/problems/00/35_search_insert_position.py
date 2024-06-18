class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        LB = 0
        UB = len(nums)
        MID = None
        while LB + 1 < UB:
            MID = (LB + UB) // 2
            print(f"{LB=} {MID=} {UB=}")
            test = nums[MID]
            print(f"  {test} <=> {target}")
            if test == target:
                print(f"Found {MID}")
                return MID
            elif test < target:
                LB = MID
            elif test > target:
                UB = MID
            else:
                assert ValueError('(test <=> target) false')
        print(f"{LB=} {MID=} {UB=}")
        print(f"Missing, using {UB}")
        return UB

