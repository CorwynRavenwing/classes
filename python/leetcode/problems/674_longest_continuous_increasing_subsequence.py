class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums:
            # empty list: no sequences
            return 0
        
        incr_L = list([
            (
                '+'
                if val > nums[i - 1]
                else ' '
            )
            for i, val in enumerate(nums)
            if i > 0
        ])
        # print(f"{incr_L=}")
        incr_S = ''.join(incr_L)
        # print(f"{incr_S=}")
        while '  ' in incr_S:
            incr_S = incr_S.replace('  ', ' ')
        # print(f"{incr_S=}")
        groups = incr_S.split(' ')
        # print(f"{groups=}")
        lengths = list(map(len, groups))
        # print(f"{lengths=}")
        best = max(lengths)
        return best + 1

