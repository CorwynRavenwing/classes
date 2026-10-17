class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        Square = lambda N: (N * N)

        answer = 0
        for i, value in enumerate(nums):
            print(f'[{i}]={value}')
            frag = {value}
            answer += Square( len(frag) )
            print(f'  0:len={len(frag)} {answer=}')
            for j, value in enumerate(nums[i+1:]):
                frag.add(value)
                answer += Square( len(frag) )
                print(f'  {j+1}:len={len(frag)} {answer=}')
        
        return answer

# NOTE: Acceptance Rate 80.3% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 148 ms Beats 12.61%
# NOTE: Memory 19.18 MB Beats 91.08%
