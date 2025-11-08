class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        answer = 0
        for i in range(len(nums)):
            subarray = nums[i:i+3]
            print(f'[{i}]: {subarray}')
            if len(subarray) != 3:
                break
            (A, B, C) = subarray
            if (A + A + C + C) == B:
                print(f'  Yes')
                answer += 1
            else:
                print(f'  no')
                
        return answer

# NOTE: Acceptance Rate 62.1% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 71 ms Beats 5.60%
# NOTE: Memory 17.94 MB Beats 27.19%

# NOTE: re-ran for challenge:
# NOTE: Runtime 79 ms Beats 7.34%
# NOTE: Memory 17.86 MB Beats 47.26%
