class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        @cache
        def maxOpsRangeScore(score: int, nums: List[int], depth=0) -> int:
            M = '  ' * depth
            print(f'{M}maxOpsRangeScore({score},{len(nums)})')
            if len(nums) < 2:
                return 0

            answers = [
                (
                    (1 + maxOpsRangeScore(score, nums[2:], depth+1))
                    if sum(nums[:2]) == score
                    else 0
                ),
                (
                    (1 + maxOpsRangeScore(score, nums[1:-1], depth+1))
                    if nums[0] + nums[-1] == score
                    else 0
                ),
                (
                    (1 + maxOpsRangeScore(score, nums[:-2], depth+1))
                    if sum(nums[-2:]) == score
                    else 0
                ),
            ]
            print(f'{M}{answers=}')
            return max(answers)
        
        if len(nums) < 2:
            return 0
        
        scores = {
            nums[0] + nums[1],
            nums[0] + nums[-1],
            nums[-2] + nums[-1],
        }
        print(f'{scores=}')
        answers = [
            maxOpsRangeScore(score, tuple(nums))
            for score in scores
        ]
        print(f'{answers=}')

        return max(answers)

# NOTE: Runtime 129 ms Beats 96.79%
# NOTE: Memory 40.78 MB Beats 93.32%
