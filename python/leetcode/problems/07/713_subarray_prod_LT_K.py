class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        i = 0
        j = 0
        product = nums[0]
        answer = 0
        # i and j define the window [i .. j] or [i:j + 1].
        # Because we need non-empty subarrays, i <= j.
        while i <= j < len(nums):
            print(f'[{i}..{j}]: {product}')
            if product < k:
                # print(f'  Yes: expand to right')
                answer += (j - i + 1)   # all subarrays ending at j
                j += 1
                try:
                    product *= nums[j]
                except IndexError:
                    # print(f'  Ran off the right end')
                    break
                continue
            else:
                # print(f'  No: contract from left')
                # don't change answer
                product //= nums[i]
                i += 1
                if i > j:
                    # print(f'  Bump to right')
                    j += 1
                    try:
                        product *= nums[j]
                    except IndexError:
                        # print(f'  Ran off the right end')
                        break
                continue
        return answer

# NOTE: Runtime 907 ms Beats 5.02%
# NOTE: Memory 18.98 MB Beats 97.84%
