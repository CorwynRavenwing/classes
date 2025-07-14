class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        by_Kth_score = lambda L: L[k]
        return sorted(
            score,
            key=by_Kth_score,
            reverse=True
        )

# NOTE: Acceptance Rate 85.7% (medium)

# NOTE: one-line answer, unrolled for legibility
# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 4 ms Beats 33.88%
# NOTE: Memory 22.57 MB Beats 85.79%
