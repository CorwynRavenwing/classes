class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if max(nums) >= target:
            return 1
        
        if sum(nums) < target:
            return 0
        
        answer = None
        total = 0
        i = 0
        iVal = nums[i]
        total += iVal
        j = 0
        while True:
            length = j - i + 1
            j = max(i, j)
            # print(f'[{i}..{j}] L={length} T={total}/{target}')
            if total < target:
                j = j + 1
                if j >= len(nums):
                    print(f'{j=} >= {len(nums)}: stop')
                    break
                jVal = nums[j]
                total += jVal
            else:
                answer = (
                    min(answer, length)
                    if answer is not None
                    else length
                )
                # total >= target
                total -= iVal   # delete current I val
                i += 1          # shrink window
                if i >= len(nums):
                    print(f'{i=} >= {len(nums)}: stop')
                    break
                iVal = nums[i]  # don't add to total

        return answer

