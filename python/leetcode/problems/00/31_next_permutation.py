class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        def sort_starting_at(ptr: int) -> None:
            nonlocal nums
            # also changes nums in-place, returning nothing
            while ptr < len(nums) - 1:
                print(f'sorting range {nums[ptr:]}')
                MP = ptr
                MN = nums[MP]
                for P in range(ptr + 1, len(nums)):
                    if MN > nums[P]:
                        MN = nums[P]
                        MP = P
                print(f'  minimum value nums[{MP}]={MN}')
                (nums[ptr], nums[MP]) = (nums[MP], nums[ptr])
                print(f'     sorted = {nums[ptr:]}')
                ptr += 1
            return
        
        # 0. If length of list is 0 or 1, return it as-is
        #    because you can't sort empty or 1-element lists
        if (not nums) or (len(nums) == 1):
            return
        
        # 1. Find section at right that is decreasing (or same).
        #    Everything left of that, stays the same.
        ptr = len(nums) - 1
        print(f'{ptr=}')
        while ptr and (nums[ptr - 1] >= nums[ptr]):
            ptr -= 1
            print(f'{ptr=}')
        
        print(f'{nums[ptr:]=}')

        if not ptr:
            # entire list is in reverse order.  "next" == sorted list.
            sort_starting_at(ptr)
            return
        
        # 2. find "next" value greater than pivot, swap it to be next
        pivot = ptr - 1
        PV = nums[pivot]
        MP = ptr
        MN = nums[MP]
        print(f'pivot at {nums[pivot]}; {nums[ptr:]}')
        for P in range(ptr + 1, len(nums)):
            if MN > nums[P] > PV:
                MN = nums[P]
                MP = P
        print(f'  minimum value > {PV} nums[{MP}]={MN}')
        (nums[pivot], nums[MP]) = (nums[MP], nums[pivot])
        print(f'after pivot: {nums[pivot:]}')

        # 3. sort everything after the pivot
        sort_starting_at(ptr)
        return
        """
        Do not return anything, modify nums in-place instead.
        """

