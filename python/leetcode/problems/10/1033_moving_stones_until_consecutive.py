class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        (x, y, z) = sorted([a, b, c])

        print(f'{a},{b},{c} (sort)-> {x},{y},{z}')

        fastest = None
        slowest = None

        if x + 1 == y and y + 1 == z:
            # case 1: already consectutive
            fastest = 0
            slowest = 0
        elif x + 1 == y:
            # case 2a: x and y already adjacent
            fastest = 1
            slowest = z - (y + 1)     # move z down by 1 until z == y + 1
        elif y + 1 == z:
            # case 2b: y and z already adjacent
            fastest = 1
            slowest = y - (x + 1)     # move x up by 1 until y == x + 1
        elif x + 2 == y:
            # case 3a: x and y are separated by 1 space
            fastest = 1             # jump between them
            # slowest = (z - (y + 1)) + (y - (x + 1))   # both prior 'slowest' formulas
            # === (z -y -1 +y -x -1)
            # === (z -y +y -x -1 -1)
            # === (z - x - 2)
            slowest = z - x - 2
        elif y + 2 == z:
            # case 3b: y and z are separated by 1 space
            fastest = 1             # jump between them
            slowest = z - x - 2
        else:
            # case 4: any other configuration
            fastest = 2             # jump x beside y, then z beside y
            slowest = z - x - 2

        return [fastest, slowest]

