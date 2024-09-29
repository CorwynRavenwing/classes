class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # We're using Floyd's loop-finding algorithm, but with a twist,
        # because we know for a fact that there is a loop, and we're
        # trying to locate it, rather than prove whether it exists.

        tortoise = 0
        hare = 0
        print(f'{tortoise=}\t{hare=}')

        tortoise = nums[tortoise]
        hare = nums[hare]
        print(f'\t\t\t{hare=}')
        hare = nums[hare]
        print(f'{tortoise=}\t{hare=}')
        
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            print(f'\t\t\t{hare=}')
            hare = nums[hare]
            print(f'{tortoise=}\t{hare=}')

        print(f'Found a loop at {tortoise}')

        footprints = set()
        while hare not in footprints:
            footprints.add(hare)
            hare = nums[hare]
            print(f'\t\t\t{hare=}')
        
        print(f'Loop == {footprints}')
        if len(footprints) == 1:
            return hare

        hare = 0
        print(f'\t\t\t{hare=}')
        while hare not in footprints:
            hare = nums[hare]
            print(f'\t\t\t{hare=}')

        return hare

# NOTE: Accepted on first Submit
# NOTE: Runtime 749 ms Beats 5.04%
# NOTE: Memory 33.01 MB Beats 12.67%
