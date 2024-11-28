class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:

        SHOW_ARRAY = lambda A: (
            f'{A}'
            if len(A) <= 3
            else
            f'[{nums[0]}..{nums[-1]}]<L={len(nums)}>'
        )
        print(f'mC({SHOW_ARRAY(nums)},{k})')

        # INTUITION: the answer to this question is:
        # (A) the minimum legal(*) value in the array, plus
        # (B) the result of a recursive call to mC(new_nums, k - 1)
        #   where new_nums === nums[] to the right of the chosen value
        # (C) with the caveat that if there aren't enough (at least k-1)
        #   values in new_nums, that the value chosen in (A) is not legal.

        if len(nums) < k:
            # not "legal" as above.
            return None
        
        if len(nums) == k:
            # exactly enough numbers.
            return nums
        
        if k == 0:
            # need a list of zero numbers.
            return []
        
        for N in sorted(set(nums)):
            # try them in numerical order, only once per value
            index = nums.index(N)
            new_nums = nums[index + 1:]
            print(f'  try {N=} {index=}: {SHOW_ARRAY(new_nums)}')
            recursive = self.mostCompetitive(
                new_nums,
                k - 1
            )
            if recursive is not None:
                print(f'  -> {N} + {SHOW_ARRAY(recursive)}')
                return [N] + recursive
        
        return None

# NOTE: recursive version gives Memory Limit Exceeded.
