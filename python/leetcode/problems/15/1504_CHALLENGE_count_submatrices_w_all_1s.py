class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        M = len(mat)
        N = len(mat[0])

        SUM = lambda a, b: ((a + b) if b else 0)
        gridSums = [
            tuple(accumulate(row, SUM))
            for row in mat
        ]
        print(f'{gridSums=}')

        answers = []
        for X in range(M):
            for Y in range(N):
                value = gridSums[X][Y]
                answers.append(value)
                if not value:
                    continue
                for X2 in reversed(range(X)):
                    value2 = gridSums[X2][Y]
                    value = min(value, value2)
                    answers.append(value)
                    if not value:
                        break
                        
        print(f'{answers=}')
        return sum(answers)

# NOTE: Acceptance Rate 57.6% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 453 ms Beats 27.83%
# NOTE: Memory 48.26 MB Beats 5.51%

# NOTE: re-ran for challenge:
# NOTE: Runtime 455 ms Beats 22.74%
# NOTE: Memory 48.72 MB Beats 5.30%
