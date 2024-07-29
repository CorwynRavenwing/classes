class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        (startX, startY) = startPos
        (homeX, homeY) = homePos
        
        if startX <= homeX:
            firstX = startX + 1    # don't include startX
            lastX = homeX + 1      # DO include homeX (top row +1 for range)
        else:
            (firstX, lastX) = (homeX, startX)   # swap X's:
            # old startX is included, old homeX is excluded
            # but they're in the wrong order
        
        row = rowCosts[firstX:lastX]
        print(f'row costs [{firstX}, {lastX}] = ${row}')

        if startY <= homeY:
            firstY = startY + 1     # don't include startY
            lastY = homeY + 1       # DO include homeY (top col +1 for range)
        else:
            (firstY, lastY) = (homeY, startY)   # swap Y's:
            # old startY is included, old homeY is excluded
            # but they're in the wrong order
        
        col = colCosts[firstY:lastY]
        print(f'col costs [{firstY}, {lastY}] = ${col}')

        return sum(row + col)

