class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        sqrt = int(area ** 0.5)
        print(f"{area=} {sqrt=}")
        
        for W in reversed(range(1, sqrt + 1)):
            print(f"  {W=}")
            if area % W != 0:
                continue
            L = area // W
            print(f"    {L=} {L * W=} {area=}")
            assert (L * W) == area
            assert L >= W
            return [L, W]

