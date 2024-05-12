class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        first = nums[0]
        prefix = None
        print(f'- {prefix}')
        for i, N in enumerate(nums):
            if N == first + i:
                prefix = nums[:i+1]
            else:
                print(f'X {nums[:i+1]}')
                break
            print(f'{i} {prefix}')
        print(f'- {prefix}')
        target = sum(prefix)
        answer = target
        print(f'{target=} {max(nums)+2=}')
        for T in range(target, max(nums) + 2):
            print(f'{T=}: {T in nums}')
            if T not in nums:
                answer = T
                break
        return answer

