class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        answer = []
        # large numbers on odd indexes, small numbers on even indexes
        while nums:
            answer.append(nums.pop(0))
            if not nums:
                break
            answer.append(nums.pop(-1))
        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 2796 ms Beats 5.25%
# NOTE: Memory 32.94 MB Beats 7.31%
