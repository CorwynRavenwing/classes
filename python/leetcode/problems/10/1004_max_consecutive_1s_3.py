class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        L = 0
        R = 0
        windowSize = (R - L)
        zerosInWindow = 0
        bestSoFar = 0
        while R <= len(nums):
            print(f'[{L}:{R}]={zerosInWindow}')
            # print(f'  DEBUG: {windowSize=} frag={nums[L:R]}')
            if zerosInWindow <= k:
                # print(f'  {zerosInWindow} zeros <= {k}: expand window to Right')
                bestSoFar = max(bestSoFar, windowSize)  # BEFORE changing windowsize
                if R >= len(nums):
                    print(f'    Ran out of room: quit')
                    break
                right = nums[R] # BEFORE changing R
                R += 1
                windowSize = (R - L)
                if right == 0:
                    zerosInWindow += 1
            else:
                # print(f'  {zerosInWindow} zeros > {k}: shrink window from Left')
                # no need to check bestSoFar: it is getting worse here
                if L > len(nums):
                    print(f'    Ran out of room: quit')
                    break
                left = nums[L]  # BEFORE changing L
                L += 1
                windowSize = (R - L)
                if left == 0:
                    zerosInWindow -= 1
                
        return bestSoFar

# NOTE: Runtime 393 ms Beats 95.87%
# NOTE: Memory 17.38 MB Beats 6.01%
