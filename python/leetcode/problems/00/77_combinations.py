class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if k == 0:
            return {()}     # a set containing only an empty tuple
        
        prior = self.combine(n, k - 1)
        print(f'{prior=}')
        answer = set()
        for P in prior:
            M = max(P, default=0)
            for A in range(M + 1, n + 1):
                # add each possible number, greater than the list max, to the list
                answer.add(P + (A,))
        return answer

# NOTE: Accepted on first Submit
# NOTE: Runtime 1170 ms Beats 5.00%
# NOTE: Memory 107.83 MB Beats 5.94%
