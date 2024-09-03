class Solution:
    def minOperations(self, k: int) -> int:

        if k == 1:
            # sum of [1] is already >= k=1
            return 0

        answers = []
        for M in range(k // 2 + 1):
            X = 1 + M
            Y = k // X
            if X*Y < k:
                Y += 1
            N = Y - 1
            moves = M + N
            print(f'{k=} {X}*{Y}={X*Y} {X*Y >= k} {moves=}')
            answers.append(moves)

        return min(answers)

# NOTE: Accepted on first Submit
# NOTE: Runtime 402 ms Beats 5.40%
# NOTE: Memory 18.46 MB Beats 5.41%
