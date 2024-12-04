class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        # SHORTCUT: since XOR is its own inverse, if we're computing
        # something that contains something else twice, we can just
        # remove that something else by XORing it another time.
        # e.g. X[3,5] = M[3,5] xor X[3,4] xor X[2,5] ***xor [2,4]***
        # b/c 2,4 is contined within each of 3,4 and 2,5.

        # print(f'{matrix=}')
        M = len(matrix)
        N = len(matrix[0])

        X = [
            [None] * N
            for index in range(M)
        ]
        # print(f'{X=}')

        X[0][0] = matrix[0][0]
        # print(f'00 {X=}')

        for a in range(1, M):
            X[a][0] = matrix[a][0] ^ X[a - 1][0]
            # print(f'a0 {X=}')

        for b in range(1, N):
            X[0][b] = matrix[0][b] ^ X[0][b - 1]
            # print(f'0b {X=}')

        for a in range(1, M):
            for b in range(1, N):
                X[a][b] = matrix[a][b] ^ X[a - 1][b] ^ X[a][b - 1] ^ X [a - 1][b - 1]
                # print(f'ab {X=}')

        # print(f'XX {X=}')

        flattened = [
            X[a][b]
            for a in range(M)
            for b in range(N)
        ]
        flattened.sort(reverse=True)
        # print(f'{flattened=}')

        return flattened[k - 1]     # 1-basis

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded)
# NOTE: Runtime 477 ms Beats 78.95%
# NOTE: Memory 51.26 MB Beats 41.41%
