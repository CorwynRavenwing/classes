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
        # print(f'{answers=}')

        lakesByDay = {
            0: []
        }
        for i, L in enumerate(rains):
            lakesByDay.setdefault(L, [])
            lakesByDay[L].append(i)
        zeroDays = lakesByDay[0]
        # print(f'{zeroDays=}')
        driesPossible = len(zeroDays)
        del lakesByDay[0]
        # print(f'{lakesByDay=}')
        driesNeeded = sum([
            len(lakeDays) - 1
            for L, lakeDays in lakesByDay.items()
        ])
        print(f'{driesPossible=} {driesNeeded=}')
        if driesNeeded > driesPossible:
            return []
        
        # LBD_Zeros = []
        # for LBD in LBD_Tuples:
        #     (Lake, (L1, L2)) = LBD
        #     if L1 < zeroDays[0] <= zeroDays[-1] < L2:
        #         ZerosBetweenFills = zeroDays
        #     else:
        #         ZerosBetweenFills = [
        #             Z
        #             for Z in zeroDays
        #             if L1 < Z < L2
        #         ]
        #     LBD_Zeros.append(
        #         (
        #             len(ZerosBetweenFills),
        #             tuple(ZerosBetweenFills[:1]),   # only need the first one
        #             LBD,
        #         )
        #     )
        # LBD_Zeros.sort()
        # print(f'LBD_Zeros=[')

        # TRY GREEDY WAY:
        greedy_answers = answers.copy()
        greedy_zeroDays = zeroDays.copy()
        count = 0
        UNKNOWN_ANSWERS = sum([
            1
            for A in greedy_answers
            if A == UNKNOWN
        ])
        print(f'{UNKNOWN_ANSWERS=} (A)')
        for Lake, LakeDays in lakesByDay.items():
            LakeDays = LakeDays.copy()
            while len(LakeDays) > 1:
                L1 = LakeDays.pop(0)    # delete first one
                L2 = LakeDays[0]        # grab second one without deleting
                for Z in greedy_zeroDays:
                    if L1 < Z < L2:
                        count += 1
                        if count < 100:
                            print(f'Dry {Lake=} on day={Z}')
                        greedy_answers[Z] = Lake
                        greedy_zeroDays.remove(Z)
                        break
        UNKNOWN_ANSWERS = sum([
            1
            for A in greedy_answers
            if A == UNKNOWN
        ])
        print(f'{UNKNOWN_ANSWERS=} (B)')
        greedy_answers = [
            (
                FakeLake
                if A == UNKNOWN
                else A
            )
            for A in greedy_answers
        ]

        UNKNOWN_ANSWERS = sum([
            1
            for A in greedy_answers
            if A == UNKNOWN
        ])
        print(f'{UNKNOWN_ANSWERS=} (C)')

        if verifyAnswer(rains, greedy_answers):
            print(f'Greedy algorithm SUCCEEDED!')
            return greedy_answers
        else:
            print(f'Greedy algorithm produced a bad answer, try the long way')

        LBD_Tuples = [
            (Lake, tuple(LakeDays[:2]))
            for Lake, LakeDays in lakesByDay.items()
            if len(LakeDays) > 1
        ]
        # # print(f'{LBD_Tuples[:2]=}...')

        while zeroDays:
            # print(f'{LBD_Tuples[:2]=}...')
            First_Zero = None
            for i, LBD in enumerate(LBD_Tuples):
                (Lake, (L1, L2)) = LBD
                if L1 < zeroDays[0] <= zeroDays[-1] < L2:
                    ZerosBetweenFills = zeroDays
                else:
                    ZerosBetweenFills = [
                        Z
                        for Z in zeroDays
                        if L1 < Z < L2
                    ]
                newZero = (
                    len(ZerosBetweenFills),
                    tuple(ZerosBetweenFills[:1]),   # only need the first one
                    LBD,
                    i,
                )
                if First_Zero is None or First_Zero > newZero:
                    print(f'new zero {newZero}')
                    First_Zero = newZero
            if First_Zero is None:
                print(f'No other lakes to dry')
                break
            print(f'{First_Zero=}')
            (zeroCount, zeroList, (Lake, (L1, L2)), LBD_index) = First_Zero
            if zeroCount == 0:
                print(f'No way to dry {Lake=} between days {L1},{L2}')
                return []
            
            zeroIndex = zeroList[0]
            print(f'Dry {Lake=} on day={zeroIndex}')
            answers[zeroIndex] = Lake
            zeroDays.remove(zeroIndex)
            lakesByDay[Lake].remove(L1)
            del LBD_Tuples[LBD_index]

        while zeroDays:
            zeroIndex = zeroDays.pop(0)
            print(f'Dry {FakeLake=} on day={zeroIndex}')
            answers[zeroIndex] = FakeLake
            # zeroDays.remove(zeroIndex)    # we used pop() instead

        if verifyAnswer(rains, answers):
            return answers
        else:
            print(f'Answer failed!')
            return []

# NOTE: Acceptance Rate 27.8% (medium)

# NOTE: re-ran for challenge:
# NOTE: Runtime 4308 ms Beats 5.12%
# NOTE: Memory 42.59 MB Beats 21.40%
