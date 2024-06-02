class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        M = len(matrix)
        N = len(matrix[0])

        def check_block(x: int, y: int, size: int) -> bool:
            # print(f'check_block({x},{y},{size})')
            # check vertical slice at Y+size-1
            for i in range(x, x+size-1):    # this -1 is to avoid checking LR cell twice
                val = matrix[i][y+size-1] if i < M and y+size-1 < N else 'OOB'
                # print(f'  M[{i}][{y+size-1}]: {val}')
                if val != '1':
                    return False
            # check horizontal slice at X+size-1
            for j in range(y, y+size):
                val = matrix[x+size-1][j] if x+size-1 < M and j < N else 'OOB'
                # print(f'  M[{x+size-1}][{j}]: {val}')
                if val != '1':
                    return False
            return True

        answer = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                # print(f'[{i},{j}]:{val}')
                if val != '1':
                    continue
                answer = max(answer, 1)
                max_size = min(M - i, N - j)
                if (max_size * max_size) < answer:
                    # even if this block is maximal,
                    # it won't affect our answer
                    # print(f'  SKIP: max_size^2={max_size * max_size} < {answer}')
                    continue
                for size in range(2, max_size + 1):
                    check = check_block(i, j, size)
                    # print(f'  {size=} {check=}')
                    if not check:
                        break
                    answer = max(answer, size * size)
        return answer

