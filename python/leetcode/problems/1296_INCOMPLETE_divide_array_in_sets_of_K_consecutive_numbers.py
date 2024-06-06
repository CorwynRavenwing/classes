class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        # we borrow some code from #846 here:

        # groups = []
        nums.sort()
        while nums:
            # print(f'{nums[:10]=}')
            # group = []
            start = min(nums)
            # print(f'look for nums starting at {start}:')
            for i in range(k):
                number = start + i
                if number in nums:
                    # print(f'  found {number=}')
                    # group.append(number)
                    nums.remove(number)
                else:
                    print(f'  MISSING {number=}')
                    return False
            # print(f'found {group=}')
            # groups.append(group)
        # print(f'{groups=}')
        return True

# NOTE: this code works but has a timeout issue after completion

