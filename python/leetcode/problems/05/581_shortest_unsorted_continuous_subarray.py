class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        target = sorted(nums)
        correct = ''.join([
            '_' if (A == B) else 'X'
            for (A, B) in zip(nums, target)
        ])
        print(f'{correct=}')
        wrong = correct.strip('_')
        print(f'{wrong=}')
        return len(wrong)

