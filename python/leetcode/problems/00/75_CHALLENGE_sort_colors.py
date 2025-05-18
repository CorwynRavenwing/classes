class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def swap_cells(index1: int, index2: int) -> None:
            nonlocal nums
            (nums[index1], nums[index2]) = (nums[index2], nums[index1])
            return
        
        for i in range(len(nums)):
            iVal = nums[i]
            print(f'{i=} {iVal=}')
            print(f'  {nums=}')
            fragment = nums[i:]
            for target in [0, 1, 2]:
                if target in fragment:
                    if iVal == target:
                        print(f'  already {target}')
                        break
                    offset = fragment.index(target)
                    j = i + offset
                    jVal = nums[j]
                    assert jVal == target
                    print(f'  swap with {j=} {jVal=}')
                    swap_cells(i, j)
                    break
        """
        Do not return anything, modify nums in-place instead.
        """

# NOTE: re-ran for challenge:
# NOTE: Runtime 7 ms Beats 3.70%
# NOTE: Memory 18.07 MB Beats 11.82%
