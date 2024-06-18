class Solution:

    def __init__(self, m: int, n: int):
        self.M = m
        self.N = n
        self.reset()

    def flip(self) -> List[int]:
        L = len(self.matrix)
        index = random.randint(0, L - 1)
        point = self.matrix[index]
        print(f'flip(): {index}/{L} = {point}')
        del self.matrix[index]
        return point

    def reset(self) -> None:
        matrix_size = (self.M * self.N)
        points_needed = 1_000
        if matrix_size < 10 * points_needed:
            # small enough matrix: just do it
            self.matrix = [
                (x, y)
                for x in range(self.M)
                for y in range(self.N)
                if (matrix_size < 1000) or (random.randint(0, matrix_size) <= 1000)
            ]
            print(f'reset(): {len(self.matrix)} (all)')
        else:
            # too-large matrix: use sampling
            dups = 0
            self.matrix = []
            while len(self.matrix) < points_needed:
                # print(f'{len(self.matrix)}/{points_needed}:')
                x = random.randint(0, self.M - 1)
                y = random.randint(0, self.N - 1)
                point = (x, y)
                if point not in self.matrix:
                    # print(f'  {point}')
                    self.matrix.append(point)
                else:
                    print(f'  {point} dup')
                    dups += 1
            print(f'reset(): {len(self.matrix)}/{matrix_size} ({dups=})')
        return

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
