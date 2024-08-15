class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        
        def legalBlock(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < (m - 1)) and (0 <= Y < (n - 1))
        
        # Blocks are named after the cell in their Top Left corner.
        # Therefore a cell is in up to four possible blocks:
        directions = (
            (0, 0),     # the cell itself
            (-1, 0),    # one left
            (0, -1),    # one up
            (-1, -1),   # one left and one up
        )
        def cellToBlocks(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            Blocks = [
                (X + I, Y + J)
                for (I, J) in directions
            ]
            Blocks = [
                B
                for B in Blocks
                if legalBlock(B)
            ]
            return Blocks
        
        squareCountsByBlock = Counter()
        for cell in coordinates:
            for B in cellToBlocks(cell):
                squareCountsByBlock[B] += 1
        # print(f'{squareCountsByBlock=}')

        totalBlocks = (m - 1) * (n - 1)
        print(f'{totalBlocks=}')
        
        blockCounter = Counter(
            squareCountsByBlock.values()
        )
        totalCounted = sum(blockCounter.values())
        print(f'{totalCounted=}')

        blockCounter[0] = (totalBlocks - totalCounted)
        print(f'{blockCounter=}')

        return [
            blockCounter[C]
            for C in range(5)
        ]
# NOTE: Runtime 2003 ms Beats 17.24%
# NOTE: Memory 25.85 MB Beats 25.29%
