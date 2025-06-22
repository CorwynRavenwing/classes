class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        answer = []
        for index in range(0, len(nums), 3):
            frag = nums[index:index + 3]
            print(f'{frag=}')
            if not frag:
                break
            assert len(frag) == 3
            (A, B, C) = frag
            if C - A > k:
                print(f'  TOO BIG')
                return []
            else:
                answer.append(frag)
        
        return answer

# NOTE: Acceptance Rate 71.8% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Limit Exceeded)
# NOTE: Runtime 190 ms Beats 5.06%
# NOTE: Memory 33.53 MB Beats 12.24%
