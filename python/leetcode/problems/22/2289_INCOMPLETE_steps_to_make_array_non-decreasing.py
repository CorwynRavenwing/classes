class Solution:
    def totalSteps(self, nums: List[int]) -> int:

        def indexesThatSurvive(nums: List[int]) -> List[int]:
            maxLeft = tuple(accumulate(nums, max))
            # print(f'{maxLeft=}')
            return [
                index
                for (Num, Max, index) in zip(nums, maxLeft, range(len(nums)))
                if (Num == Max)
            ] + [len(nums)]
        
        def timeToDelete(nums: List[int], deleting: bool, depth=0) -> int:
            margin = '  ' * depth
            print(f'{margin}TTD({nums}):')
            ITS = indexesThatSurvive(nums)
            print(f'{margin}  {ITS=}')
            if len(nums) == len(ITS) - 1:
                if deleting:
                    print(f'{margin}->all indexes deleted: len={len(nums)} time')
                    return len(nums)
                else:
                    print(f'{margin}->all indexes survive: zero time')
                    return 0
            recurse = [
                timeToDelete(nums[A+1:B], True, depth+1)
                for (A, B) in zip(ITS, ITS[1:])
            ]
            print(f'{margin}->{recurse=}')
            return max(recurse, default=0)

        TTD = timeToDelete(nums, False)
        print(f'{TTD=}')
        return TTD
# NOTE: There are input sets that this fails to work for.
