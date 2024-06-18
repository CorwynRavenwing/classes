class Solution:
    def isGood(self, nums: List[int]) -> bool:

        print(f'unsorted {nums}')
        nums.sort()
        print(f'sorted   {nums}')
        N = len(nums)
        base_n = list(range(1,N)) + [N-1]
        print(f'base_n   {base_n}')
        return nums == base_n

