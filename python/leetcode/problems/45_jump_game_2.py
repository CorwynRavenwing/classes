class Solution:
    def jump(self, nums: List[int]) -> int:

        min_jumps = {
            0: 0
        }
        print(f'min jumps from {0} to {len(nums)-1}')
        # print(f'{nums=}')
        # print(f'i in range({0},{len(nums)}):')
        for i in range(len(nums)):
            min_jumps.setdefault(i, None)
            jumps_so_far = min_jumps[i]
            jumps_from_here = nums[i]
            # print(f'  {i=} {jumps_so_far=} {jumps_from_here=}')
            # print(f'    j in range({i + 1}, {i + jumps_from_here + 1})')
            for j in range(i + 1, i + jumps_from_here + 1):
                # print(f'      {j=}')
                min_jumps.setdefault(j, None)
                if min_jumps[j] is None or min_jumps[j] > jumps_so_far + 1:
                    min_jumps[j] = jumps_so_far + 1
                    # print(f'        min_jumps={jumps_so_far + 1}')

        return min_jumps[len(nums) - 1]

