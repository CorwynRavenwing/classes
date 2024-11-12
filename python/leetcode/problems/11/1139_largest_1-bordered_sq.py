class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        countTruncating = lambda x, y: (x + y if y else 0)
        ACC = lambda row: tuple(accumulate(row, countTruncating))
        REV = lambda x: tuple(reversed(tuple(x)))

        gREV = lambda G: tuple(map(REV, G))
        gINV = lambda G: tuple(zip(*G))
        gACC = lambda G: tuple(map(ACC, G))
        # reverse, acc, then reverse again:
        R_A_R = lambda G: gREV(gACC(gREV(G)))

        MIN_GRID = lambda G1, G2: tuple([
            tuple(map(min, zip(R1, R2)))
            for (R1, R2) in zip(G1, G2)
        ])

        countLeft = gACC(grid)
        countRight = R_A_R(grid)
        # inverse, acc, then inverse again:
        countUp = gINV(gACC(gINV(grid)))
        # inverse, (rev, acc, rev), then inverse again:
        countDown = gINV(R_A_R(gINV(grid)))

        min_RD = MIN_GRID(countRight, countDown)
        min_UL = MIN_GRID(countLeft, countUp)

        print(f'cR={countRight}')
        print(f'cD={countDown}')
        print(f'RD={min_RD}')
        print()
        print(f'cL={countLeft}')
        print(f'cU={countUp}')
        print(f'UL={min_UL}')

        maxSize = 0

        for X, row_RD in enumerate(min_RD):
            for Y, val_RD in enumerate(row_RD):
                print(f'({X},{Y}):')
                if val_RD <= maxSize:
                    # can't get any better
                    continue
                if val_RD == 1:
                    # freebie
                    maxSize = max(maxSize, 1)
                    continue
                minSize = max(2, maxSize)
                for Size in range(minSize, val_RD + 1):
                    (X2, Y2) = (X+Size-1, Y+Size-1)
                    print(f'  {Size=} ({X2},{Y2})')
                    try:
                        val_UL = min_UL[X2][Y2]
                    except IndexError:
                        print(f'    -> (OOB)')
                        continue
                    print(f'    -> {val_UL}')
                    if val_UL < Size:
                        print(f'    -> (too small)')
                        continue
                    print(f'    -> YES')
                    maxSize = max(maxSize, Size)

        return (maxSize * maxSize)  # need the square

# NOTE: Accepted on first Submit
# NOTE: Runtime 164 ms Beats 36.36%
# NOTE: Memory 17.85 MB Beats 7.75%
