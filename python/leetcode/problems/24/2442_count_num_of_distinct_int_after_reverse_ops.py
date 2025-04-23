class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        answer = set(nums)
        for N in nums:
            strN = str(N)
            strR = ''.join(reversed(strN))
            R = int(strR)
            print(f'{N} "{strN}" "{strR}" {R}')
            answer.add(R)
        
        print(answer)
        return len(answer)

# NOTE: Accepted on second Run (typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 456 ms Beats 5.12%
# NOTE: Memory 44.70 MB Beats 74.77%
