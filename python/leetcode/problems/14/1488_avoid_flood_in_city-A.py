class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        UNKNOWN = -999
        FakeLake = 1

        def verifyAnswer(rains: List[int], answer: List[int]) -> bool:
            LakeList = set()
            print(f'Verifying answer ...')
            for (LakeWet, LakeDry) in zip(rains, answer):
                print(f'  {LakeWet=} {LakeDry=}')
                if LakeWet != 0:
                    if LakeDry != -1:
                        print(f'    ERROR! must answer -1 for all non-dry days')
                        return False
                    if LakeWet in LakeList:
                        print(f'    ERROR! flood in lake {LakeWet}')
                        return False
                    LakeList.add(LakeWet)
                else:
                    # zero: dry a lake
                    if LakeDry in LakeList:
                        print(f'    dry lake {LakeDry}')
                        LakeList.remove(LakeDry)
                    elif LakeDry == FakeLake:
                        print(f'    dry {FakeLake=}')
                    else:
                        print(f'    ERROR!  Cannnot dry a dry lake besides {FakeLake=}')
                        return False
            print(f'Verified!')
            return True

        answers = [
            (
                UNKNOWN
                if R == 0
                else -1
            )
            for R in rains
        ]
        print(f'{answers=}')

        lakesByDay = {
            0: []
        }
        for i, L in enumerate(rains):
            lakesByDay.setdefault(L, [])
            lakesByDay[L].append(i)
        zeroDays = lakesByDay[0]
        print(f'{zeroDays=}')
        driesPossible = len(zeroDays)
        del lakesByDay[0]
        print(f'{lakesByDay=}')
        driesNeeded = sum([
            len(lakeDays) - 1
            for L, lakeDays in lakesByDay.items()
        ])
        print(f'{driesPossible=} {driesNeeded=}')
        if driesNeeded > driesPossible:
            return []
        
        while zeroDays:
            # pick a zero, which is followed by a non-zero, which isn't first of its type
            while zeroDays:
                zeroIndex = zeroDays[0]
                # don't pop, because we might remove a *different* zero
                print(f'{zeroIndex=}')
                lakeIndex = zeroIndex
                while (lakeIndex := lakeIndex + 1) < len(rains):
                    Lake = rains[lakeIndex]
                    print(f'  {lakeIndex=} {Lake=}')
                    if Lake == 0:
                        if lakeIndex in zeroDays:
                            # go around again, using this zero instead
                            zeroIndex = lakeIndex
                            print(f'{zeroIndex=} ++')
                            continue
                        else:
                            # go around again, skipping this zero
                            print(f'    Got this zero already')
                            continue
                    LD = lakesByDay[Lake]
                    if lakeIndex not in LD:
                        print(f'    {lakeIndex=} already done')
                        continue
                    iLake = LD.index(lakeIndex)
                    print(f'    {iLake=} {LD}')
                    if iLake == 0:
                        print(f'      {Lake=} not full yet')
                        continue
                    if iLake > 1:
                        print(f'      Strange, iLake is neither 0 nor 1')
                        return [-88888]
                    assert iLake == 1
                    lakeFilled = LD[0]
                    print(f'      {lakeFilled=} emptied={zeroIndex} refilled={lakeIndex}')
                    # answers[lakeFilled] = -1
                    answers[zeroIndex] = Lake
                    assert LD[iLake] == lakeIndex
                    del LD[iLake]   # or do I need to change lakesByDay[Lake] itself?
                    print(f'CHECK {zeroDays=}')
                    zeroDays.remove(zeroIndex)
                    print(f' DONE {zeroDays=}')
                    break
                if lakeIndex >= len(rains):
                    print(f'no rain left: {lakeIndex=} >= {len(rains)}')
                    answers[zeroIndex] = FakeLake
                    print(f'CHECK {zeroDays=}')
                    zeroDays.remove(zeroIndex)
                    print(f' DONE {zeroDays=}')

        if verifyAnswer(rains, answers):
            return answers
        else:
            print(f'Answer failed!')
            return []

# NOTE: fails for odd testcases when guessing which lake to dry
