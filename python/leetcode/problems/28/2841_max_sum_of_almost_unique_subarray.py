class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:

        partialSums = (0,) + tuple(accumulate(nums))
        # print(f'{partialSums=}')

        max_sum = 0
        counts = Counter(nums[0:k])
        for i, A in enumerate(nums):
            j = i + k - 1
            if j >= len(nums):
                # print(f'NO')
                continue    # next I
                # break       # break I
            B = nums[j]
            # print(f'[{i}..{j}] ({A},{B}) {counts=}')
            # print(f'[{i}..{j}] ({A},{B}) {len(counts)=}')
            # print(f'DEBUG: frag={nums[i:j+1]}')
            distinct = len(counts)
            if distinct >= m:
                # true: record answer
                total = partialSums[j + 1] - partialSums[i]
                # print(f'  Yes ({distinct}): new answer {total}')
                max_sum = max(max_sum, total)
            # else:
            #     # print(f'  No ({distinct})')
            # in any case: expand J to right and shrink I from left
            j += 1
            if j >= len(nums):
                break
            B = nums[j]
            # print(f'  Counts -= {A}, += {B}')
            counts[B] += 1  # AFTER updating J
            counts[A] -= 1  # BEFORE updating I
            if not counts[A]:
                del counts[A]
        
        return max_sum
# NOTE: Runtime 418 ms Beats 22.49%
# NOTE: Memory 20.86 MB Beats 14.06%
