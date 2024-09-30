class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        H = heapq.merge(*matrix)
        for i in range(k - 1):
            ignore = next(H)
        return next(H)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 156 ms Beats 47.01%
# NOTE: Memory 21.21 MB Beats 38.97%
