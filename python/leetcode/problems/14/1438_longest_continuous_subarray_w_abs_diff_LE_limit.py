from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        DEBUG = False

        I = 0
        J = I + 1
        span = SortedList(nums[I:J])
        maxLength = float('-inf')
        while 0 <= I < J <= len(nums):
            if DEBUG: print(f'[{I}:{J}] {span=}')
            (Min, Max) = (span[0], span[-1])
            diff = Max - Min
            if DEBUG: print(f'  |{Max}-{Min}| = {diff}')
            if diff <= limit:
                # good: record answer
                length = J - I
                maxLength = max(length, maxLength)
            else:
                # bad: shrink left
                span.remove(nums[I])
                I += 1
            # always expand to the right
            try:
                span.add(nums[J])
                J += 1
            except IndexError:
                break

        return maxLength

# NOTE: Accepted on second Run (first was out-of-bounds error)
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 575 ms Beats 13.35%
# NOTE: Memory 25.53 MB Beats 76.5%
