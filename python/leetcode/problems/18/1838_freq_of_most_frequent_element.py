class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        (L, R) = (0, 0)
        N = R - L
        total = 0
        maxWindowSize = 0
        highest = 0

        while L <= R <= len(nums):
            # print(f'[{L},{R}]: {N=} M={highest} T={total}')
            frag = nums[L:R]
            total_after_upgrading_window = (N * highest)
            price_of_window = total_after_upgrading_window - total
            if price_of_window <= k:
                # print(f'  YES ({price_of_window})')
                maxWindowSize = max(maxWindowSize, N)
                # move R right
                if R >= len(nums):
                    # print(f'    {R=} out of bounds!')
                    break
                highest = nums[R]
                # following loop jumps to the END of a block of same number [highest]
                while R < len(nums) and highest == nums[R]:
                    R += 1      # AFTER we reference it above
                    total += highest
                    N += 1
            else:
                # print(f'  NO ({price_of_window})')
                # move L right
                lowest = nums[L]
                L += 1      # AFTER we reference it above
                total -= lowest
                N -= 1

        return maxWindowSize

