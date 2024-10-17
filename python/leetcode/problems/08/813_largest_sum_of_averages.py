class Solution:

    @cache
    def Average(self, nums: List[int]) -> float:
        if not nums:
            return 0

        return sum(nums) / len(nums)
    
    @cache
    def LSOA(self, nums: List[int], k: int) -> float:
        # print(f'LSOA({nums},{k}):')
        print(f'LSOA(L={len(nums)},{k}):')
        if k == 1:
            answer = self.Average(nums)
            # print(f'  {nums}\n\tAvg={answer}')
            print(f'\tAvg={answer}')
            return answer
        
        subAnswers = [
            (
                self.Average(nums[:i]),
                self.LSOA(nums[i:], k - 1),
            )
            for i in range(1, len(nums))
        ]
        # print(f'  {nums}\n\tSub={subAnswers}')
        print(f'\tSub={subAnswers}')
        answer = max(map(sum, subAnswers), default=0)
        print(f'\tAns={answer}')
        return answer

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # passed-in variable needs to be hashable:
        return self.LSOA(tuple(nums), k)

# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 959 ms Beats 5.06%
# NOTE: Memory 39.61 MB Beats 5.06%
