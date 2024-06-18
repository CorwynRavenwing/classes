class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if k > len(nums):
            print(f'{k=} mod {len(nums)}', end=' ')
            k %= len(nums)
            print(f'-> {k}')
        
        while k:
            print(f'  rotate {k=}')
            k -= 1
            nums.insert(0, nums.pop())
        
        return
        """
        Do not return anything, modify nums in-place instead.
        """

