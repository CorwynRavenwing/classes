class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:

        if k == 0:
            print(f'A: {k=}')
            if nums:
                # no moves, return first element
                return nums[0]
            else:
                # no elements, list will be empty
                return -1
        elif k == 1:
            print(f'B: {k=}')
            if len(nums) > 1:
                # one move, return *second* element
                return nums[1]
            else:
                # one move will delete only element, list will be empty
                return -1
        elif len(nums) == 1:
            print(f'C: {len(nums)=}')
            if k % 2 == 0:
                print(f'  (even)')
                return nums[0]
            else:
                print(f'  (odd)')
                return -1
        elif len(nums) > k:
            print(f'D: len(nums) > {k}')
            return max(
                max(nums[:k-1]),    # delete first k-1, push largest back
                nums[k]             # delete first k: number [k] remains
            )
        elif len(nums) == k:
            print(f'E: len(nums) = {k}')
            return max(nums[:k-1])  # delete all but 1, push largest back
        else:
            print(f'F: otherwize')
            return max(nums)        # delete everything, twiddle till k-1, push max
# NOTE: Runtime 424 ms Beats 88.64%
# NOTE: Memory 30.40 MB Beats 60.4%
