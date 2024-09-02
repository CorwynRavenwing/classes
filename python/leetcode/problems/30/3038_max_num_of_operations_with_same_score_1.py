class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        # we borrow some code from #3040, which I did first
        # and comment out the operations #2 and #3 which aren't valid here

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
                # (
                #     (1 + maxOpsRangeScore(score, nums[1:-1], depth+1))
                #     if nums[0] + nums[-1] == score
                #     else 0
                # ),
                # (
                #     (1 + maxOpsRangeScore(score, nums[:-2], depth+1))
                #     if sum(nums[-2:]) == score
                #     else 0
                # ),
            ]
            print(f'{M}{answers=}')
            return max(answers)
        
        if len(nums) < 2:
            return 0
        
        scores = {
            nums[0] + nums[1],
            # nums[0] + nums[-1],
            # nums[-2] + nums[-1],
        }
        print(f'{scores=}')
        answers = [
            maxOpsRangeScore(score, tuple(nums))
            for score in scores
        ]
        print(f'{answers=}')

        return max(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 55 ms Beats 5.95%
# NOTE: Memory 16.78 MB Beats 26.21%
