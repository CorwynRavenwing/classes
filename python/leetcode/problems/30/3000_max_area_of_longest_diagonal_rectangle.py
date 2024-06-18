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


        return 000000
        
