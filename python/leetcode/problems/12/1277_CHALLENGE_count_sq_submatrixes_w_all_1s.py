class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        Squared = lambda x: x * x
        
        partialSums = [
            (0,) + tuple(accumulate(row))
            for row in matrix
        ]
        print(f'{partialSums=}')

        ones = {
            (X, Y)
            for X, row in enumerate(matrix)
            for Y, val in enumerate(row)
            if val == 1
        }
        # print(f'{ones=}')
        answer = len(ones)

        size = 2
        squares = ones
        while squares:
            print(f'{size=}')
            SQ = Squared(size)
            print(f'  {SQ=}')
            new_squares = set()
            for S in squares:
                print(f'  {S=}')
                (X, Y) = S
                try:
                    sums = [
                        partialSums[X + Z][Y + size] - partialSums[X + Z][Y]
                        for Z in range(size)
                    ]
                except IndexError:
                    continue
                print(f'    {sums=}')
                if sum(sums) == SQ:
                    new_squares.add(S)
                    print(f'    {S=} {size=}')
            squares = new_squares
            answer += len(squares)
            size += 1

        return answer

# NOTE: Acceptance Rate 79.1% (medium)

# NOTE: Accepted on first Submit
# NOTE: Runtime 460 ms Beats 5.80%
# NOTE: Memory 24.63 MB Beats 6.82%

# NOTE: re-ran for challenge:
# NOTE: Runtime 475 ms Beats 5.04%
# NOTE: Memory 25.69 MB Beats 11.27%
