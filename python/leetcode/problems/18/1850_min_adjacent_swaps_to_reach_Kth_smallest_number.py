class Solution:

    # we borrow some code from #31:

    # this version returns a new value rather than sorting in place:
    def nextPermutation(self, nums: List[int]) -> List[int]:

        def sort_starting_at(ptr: int) -> None:
            nonlocal nums
            nums = nums[:ptr] + list(sorted(nums[ptr:]))
            # while ptr < len(nums) - 1:
            #     # print(f'sorting range {nums[ptr:]}')
            #     MP = ptr
            #     MN = nums[MP]
            #     for P in range(ptr + 1, len(nums)):
            #         if MN > nums[P]:
            #             MN = nums[P]
            #             MP = P
            #     # print(f'  minimum value nums[{MP}]={MN}')
            #     (nums[ptr], nums[MP]) = (nums[MP], nums[ptr])
            #     # print(f'     sorted = {nums[ptr:]}')
            #     ptr += 1
            return

        # 0. If length of list is 0 or 1, return it as-is
        #    because you can't sort empty or 1-element lists
        if (not nums) or (len(nums) == 1):
            return nums

        # 1. Find section at right that is decreasing (or same).
        #    Everything left of that, stays the same.
        ptr = len(nums) - 1
        # print(f'{ptr=}')
        while ptr and (nums[ptr - 1] >= nums[ptr]):
            ptr -= 1
            # print(f'{ptr=}')

        # print(f'{nums[ptr:]=}')

        if not ptr:
            # entire list is in reverse order.  "next" == sorted list.
            sort_starting_at(ptr)
            return

        # 2. find "next" value greater than pivot, swap it to be next
        pivot = ptr - 1
        PV = nums[pivot]
        MP = ptr
        MN = nums[MP]
        # print(f'pivot at {nums[pivot]}; {nums[ptr:]}')
        for P in range(ptr + 1, len(nums)):
            if MN > nums[P] > PV:
                MN = nums[P]
                MP = P
        # print(f'  minimum value > {PV} nums[{MP}]={MN}')
        (nums[pivot], nums[MP]) = (nums[MP], nums[pivot])
        # print(f'after pivot: {nums[pivot:]}')

        # 3. sort everything after the pivot
        sort_starting_at(ptr)

        return nums

    def getMinSwaps(self, num: str, k: int) -> int:
        print(f'-: {num}')
        num = list(map(int, num))
        orig_num = num[:]   # copy
        for _ in range(k):
            num = self.nextPermutation(num)
            # print(f'{_}: {"".join(map(str, num))}')
        print(f'{_}: {"".join(map(str, num))}')
        print('---' + '-' * len(num))
        
        swaps = 0
        print(f'{swaps}: A={"".join(map(str, num))}' + ' (num)')
        print(f'{swaps}: B={"".join(map(str, orig_num))}' + ' (orig_num)')
        for i, A in enumerate(num):
            B = orig_num[i]
            if A == B:
                # print(f'  DEBUG:[{i}] match {A} {B}')
                continue
            # print(f'  DEBUG:[{i}] mis-match {A} {B}')
            # print(f'  DEBUG:[{i}] seek "{A}" in {orig_num[i + 1:]}')
            j = orig_num.index(A, i + 1)
            # print(f'  swap [{i}]{A} [{j}]{B}')
            swaps += (j - i)
            beforeA = orig_num[:i]
            betweenAB = orig_num[i + 1:j]
            afterB = orig_num[j + 1:]
            assert orig_num == beforeA + [B] + betweenAB + [A] + afterB
            orig_num = beforeA + [A, B] + betweenAB + afterB
            print(f'{swaps}: A={"".join(map(str, num))}' + ' (num)')
            print(f'{swaps}: B={"".join(map(str, orig_num))}' + ' (orig_num)')
            assert A == orig_num[i]

        assert orig_num == num
        return swaps

# NOTE: with manual sort-in-place: 5000ms
# NOTE: with built-in sort and return: 63ms == 100x faster

# NOTE: Accepted on third Submit (Time Exceeded: use built-in sort)
# NOTE: Runtime 790 ms Beats 46.00%
# NOTE: Memory 18.00 MB Beats 5.17%
