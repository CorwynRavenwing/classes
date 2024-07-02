class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:

        def NchooseK(N: int, K: int) -> int:
            # general formula == N! / (K! * (N-K)!)
            # we only need to handle K of 2 or 3 here
            if K == 2:
                return (N) * (N - 1) // 2
            if K == 3:
                return (N) * (N - 1) * (N - 2) // 6
        
        countArr = Counter(arr)
        print(f'{countArr=}')
        possibles = [
            (1, ())     # one possibility: no numbers
        ]
        answer = 0
        # print(f'Poss={len(possibles)}')
        for A, Acount in countArr.items():
            # print(f'  try {A=}')
            new_possibles = []
            for P in possibles:
                (Gcount, group) = P
                # print(f'    {P} + {A}')
                # Add 1 copy of A
                groupPlus1 = group + (A,)
                countPlus1 = Gcount * Acount
                if (len(groupPlus1) == 3):
                    if (sum(groupPlus1) == target):
                        answer += countPlus1
                    continue
                Pplus1 = (countPlus1, groupPlus1)
                new_possibles.append(Pplus1)
                if len(group) <= 1:
                    # can add 2 units
                    if Acount < 2:
                        # dont have 2 units to add
                        continue
                    # add 2 copies of A
                    groupPlus2 = group + (A, A)
                    countPlus2 = Gcount * NchooseK(Acount, 2)
                    if (len(groupPlus2) == 3):
                        if (sum(groupPlus2) == target):
                            answer += countPlus2
                        continue
                    Pplus2 = (countPlus2, groupPlus2)
                    new_possibles.append(Pplus2)

                if len(group) <= 0:
                    # can add 3 units
                    if Acount < 3:
                        # dont have 3 units to add
                        continue
                    # add 3 copies of A
                    groupPlus3 = group + (A, A, A)
                    countPlus3 = Gcount * NchooseK(Acount, 3)
                    if (len(groupPlus3) == 3):
                        if (sum(groupPlus3) == target):
                            answer += countPlus3
                        continue
                    assert "we never" == "get here"
                    Pplus3 = (countPlus3, groupPlus3)
                    new_possibles.append(Pplus3)

            possibles.extend(new_possibles)
            # print(f'Poss={len(possibles)}')
        
        mod = 10 ** 9 + 7
        answer %= mod
        return answer

