class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        answer = set()

        start = nums[0] - k - 1

        for N in nums:
            print(f'{N}:')
            start = max(start, N - k)
            end = N + k
            loops = 0
            for X in range(start, end + 1):
                loops += 1
                if X not in answer:
                    print(f'-> {X} ({loops})')
                    answer.add(X)
                    break
                else:
                    start = X
        
        return len(answer)

# NOTE: Acceptance Rate 32.4% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Time Exceeded)
# NOTE: Runtime 1395 ms Beats 5.33%
# NOTE: Memory 36.68 MB Beats 35.50%
