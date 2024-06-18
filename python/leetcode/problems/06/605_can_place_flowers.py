class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        available_plot = '000'
        flowerbed = [0] + flowerbed + [0]
        while n:
            F = ''.join(map(str, flowerbed))
            # print(f"{n=} {F=}")
            if available_plot in F:
                index = F.index(available_plot)
                flowerbed[index + 1] = 2
                n -= 1
            else:
                return False
        F = ''.join(map(str, flowerbed))
        # print(f"{n=} {F=} {flowerbed=}")
        return True

