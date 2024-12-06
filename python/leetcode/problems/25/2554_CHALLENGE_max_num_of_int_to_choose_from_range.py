class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banSet = {
            B
            for B in banned
            if B <= n
        }
        
        # greedy algorithm, smallest numbers first
        count = 0
        total = 0
        for i in range(1, n + 1):
            if i in banSet:
                continue
            total += i
            if total > maxSum:
                break

            count += 1
        
        return count

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 48 ms Beats 58.77%
# NOTE: Memory 19.05 MB Beats 7.35%
