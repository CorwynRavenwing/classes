class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        def check_increasing(nums: List[int]) -> str:
            pairs = tuple(zip(nums, nums[1:]))
            # print(f'{pairs=}')

            direction = tuple(
                (
                    '+'
                    if B > A
                    else
                    '-'
                )
                for (A, B) in pairs
            )
            # print(f'{direction=}')
            return ''.join(direction)
        
        check = check_increasing(nums)
        print(f'{check=}')
        if '-' not in check:
            return True

        index = check.index('-')
        print(f'{index=}')

        if index > 0:
            new_nums = nums.copy()
            del new_nums[index - 1]
            print(f'{new_nums=}')
            check = check_increasing(new_nums)
            print(f'{check=}')
            if '-' not in check:
                return True

        new_nums = nums.copy()
        del new_nums[index]
        print(f'{new_nums=}')
        check = check_increasing(new_nums)
        print(f'{check=}')
        if '-' not in check:
            return True

        if index + 1 < len(nums):
            new_nums = nums.copy()
            del new_nums[index + 1]
            print(f'{new_nums=}')
            check = check_increasing(new_nums)
            print(f'{check=}')
            if '-' not in check:
                return True

        return False

