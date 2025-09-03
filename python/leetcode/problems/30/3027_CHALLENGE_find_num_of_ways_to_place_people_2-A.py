class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        # we borrow some code from #3025:

        points = tuple(map(tuple, points))  # each points must be hashable
        # print(f'{points=}')
        pointsX = {}
        pointsY = {}
        for P in points:
            (X, Y) = P
            pointsX.setdefault(X, set())
            pointsY.setdefault(Y, set())
            pointsX[X].add(P)
            pointsY[Y].add(P)

        UNION = lambda x, y: x | y
        ACC = lambda x: tuple(accumulate(tuple(x), UNION))
        REV = lambda x: tuple(reversed(tuple(x)))

        # print()
        # print(f'X={tuple(pointsX.items())}')
        keysX = tuple(sorted(pointsX.keys()))
        valsX = [
            pointsX[X]
            for X in keysX
        ]
        # print(f'{keysX=}')
        # print(f'{valsX=}')
        accXL = ACC(valsX)
        accXR = REV(ACC(REV(valsX)))
        # print(f'{accXL=}')
        # print(f'{accXR=}')

        # Right_of_X = dict(zip(keysX, accXR[1:]))
        # Right_of_X[keysX[-1]] = set()
        Right_of_X = dict(zip(keysX, accXR))
        # print(f'{Right_of_X=}')
        # Left_of_X = dict(zip(keysX[1:], accXL[:-1]))
        # Left_of_X[keysX[0]] = set()
        Left_of_X = dict(zip(keysX, accXL))
        # print(f'{Left_of_X=}')

        # print()
        # print(f'Y={tuple(pointsY.items())}')
        keysY = tuple(sorted(pointsY.keys()))
        valsY = [
            pointsY[Y]
            for Y in keysY
        ]
        # print(f'{keysY=}')
        # print(f'{valsY=}')
        accYL = ACC(valsY)
        accYR = REV(ACC(REV(valsY)))
        # print(f'{accYL=}')
        # print(f'{accYR=}')

        # Up_of_Y = dict(zip(keysY, accYR[1:]))
        # Up_of_Y[keysY[-1]] = set()
        Up_of_Y = dict(zip(keysY, accYR))
        # print(f'{Up_of_Y=}')
        # print(f'making Down_of_Y : zip({keysY[1:]},{accYL[:-1]})')
        # Down_of_Y = dict(zip(keysY[1:], accYL[:-1]))
        # Down_of_Y[keysY[0]] = set()
        Down_of_Y = dict(zip(keysY, accYL))
        # print(f'{Down_of_Y=}')

        print()
        answer = 0
        for UL in points:
            print(f'{UL=}')
            (X1, Y1) = UL
            R_set = Right_of_X[X1]
            D_set = Down_of_Y[Y1]
            DR_set = R_set & D_set     # "&" == intersection
            DR_set -= {UL}     # don't count the upper-left point itself

            # print(f'  {DR_set=}')
            for DR in DR_set:
                # print(f'  {DR=}')
                (X2, Y2) = DR
                L_set = Left_of_X[X2]
                U_set = Up_of_Y[Y2]
                UL_set = L_set & U_set
                in_box = (
                    DR_set & UL_set
                ) - (
                    {UL, DR}    # don't count the corners themselves
                )
                if len(in_box):
                    # print(f'    No: {len(in_box)} in box')
                    continue
                else:
                    answer += 1
                    # print(f'    Yes: ({answer})')

        return answer

# NOTE: getting TLE for huge inputs: need a more efficient algorithm
