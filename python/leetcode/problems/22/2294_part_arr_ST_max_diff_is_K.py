class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        # could deduplicate nums here if we chose

        nums.sort()

        answer = 1
        low = None
        for N in nums:
            print(f'{answer:4d} {low}:{N=}')
            if low is None:
                low = N
                continue
            
            if N - low > k:
                print(f'  new partition')
                answer += 1
                low = N

        return answer

# NOTE: Acceptance Rate 74.3% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 469 ms Beats 5.02%
# NOTE: Memory 29.56 MB Beats 11.07%
