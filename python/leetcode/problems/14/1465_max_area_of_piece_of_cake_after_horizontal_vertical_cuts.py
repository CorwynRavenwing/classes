class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def maxDistance(cuts: List[int]) -> int:
            cuts.sort()
            print(f'{cuts=}')
            distances = [
                B - A
                for (A, B) in zip(cuts, cuts[1:])
            ]
            print(f'{distances=}')
            return max(distances)
        
        maxX = maxDistance(horizontalCuts + [0, h])
        maxY = maxDistance(verticalCuts + [0, w])
        print(f'Dimensions {maxX=},{maxY=}')
        mod = 10 ** 9 + 7
        return (maxX * maxY) % mod
# NOTE: 236 ms; Beats 76.84%
