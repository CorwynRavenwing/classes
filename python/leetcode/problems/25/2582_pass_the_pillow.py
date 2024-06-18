class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        dirLabel = {
            1: 'R',
            -1: 'L',
        }
        pillow = 1
        direction = 1
        print(f"t={0}/{time} {pillow} {dirLabel[direction]} {n}")
        for t in range(1, time+1):
            pillow += direction
            if pillow in [1, n]:
                direction *= -1
            print(f"{t=}/{time} {pillow} {dirLabel[direction]} {n}")
        return pillow

