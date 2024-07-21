class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:

        partialSums = list(itertools.accumulate(nums))

        # startIndex and endIndex are INCLUSIVE here
        # @cache
        def spaceWasted(startIndex: int, endIndex: int) -> int:
            nonlocal nums
            if startIndex >= len(nums):
                return 0
            # print(f'  spaceWasted({startIndex},{endIndex})')
            frag = nums[startIndex:endIndex+1]
            len_frag = endIndex - startIndex + 1
            max_frag = max(frag)
            sum_before = (partialSums[startIndex - 1] if startIndex else 0)
            sum_frag = partialSums[endIndex] - sum_before
            # print(f'    = len={len_frag} * max={max_frag} - sum={sum_frag}')
            return len_frag * max_frag - sum_frag

        @cache
        def minSpaceWasted(startIndex: int, kRemaining: int) -> int:
            nonlocal nums
            if startIndex >= len(nums):
                return 0
            if not kRemaining:
                return spaceWasted(startIndex, len(nums) - 1)
            # print(f'minSpaceWasted({startIndex},{kRemaining})')
            answers = [
                sum([
                    spaceWasted(startIndex, endIndex),      # may be equal for 1-digit ranges
                    minSpaceWasted(endIndex + 1, kRemaining - 1),
                ])
                for endIndex in range(startIndex, len(nums))
            ]
            # print(f'{answers=}')
            return min(answers)
        
        return minSpaceWasted(0, k)

