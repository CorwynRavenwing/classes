class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        print(f'{dimensions=}')

        rectangles = [
            (
                (L*L + W*W) ** 0.5, # diagonal == hypotenuse
                L * W               # area
            )
            for (L, W) in dimensions
        ]
        print(f'{rectangles}')
        rectangles.sort(reverse=True)
        winner = rectangles[0]
        print(f'{winner=}')
        (diag, area) = winner
        return area


# NOTE: Acceptance Rate 36.8% (easy)

# NOTE: re-ran for challenge:
# NOTE: Runtime 14 ms Beats 5.88%
# NOTE: Memory 18.28 MB Beats 22.60%
