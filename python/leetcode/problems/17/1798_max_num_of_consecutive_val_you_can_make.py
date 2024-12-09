class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        
        best = 0
        for C in sorted(coins):
            if C <= best + 1:
                best += C
            else:
                break
        return best + 1

# NOTE: Accepted on second Run (fencepost error)
# NOTE: Accepted on first Submit
# NOTE: Runtime 59 ms Beats 35.20%
# NOTE: Memory 21.54 MB Beats 27.56%
