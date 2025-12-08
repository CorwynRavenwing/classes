from itertools import combinations

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        def Nchoose2(N: int) -> int:
            return N * (N - 1) // 2

        mod = 10 ** 9 + 7

        Xs_by_Y = Counter()
        for (x, y) in points:
            Xs_by_Y[y] += 1
        # print(f'{Xs_by_Y=}')

        X_values_by_Y = [
            Nchoose2(x_count)
            for x_count in Xs_by_Y.values()
            if x_count >= 2
        ]
        # print(f'{X_values_by_Y=}')

        answer = 0
        # print(f'(begin) {answer=}')
        for (a, b) in combinations(X_values_by_Y, 2):
            answer += (a * b)
            answer %= mod
            # print(f'({a},{b}) {answer=}')

        return answer % mod

# NOTE: Acceptance Rate 47.0% (medium)

# NOTE: Time Limit Exceeded for large inputs
