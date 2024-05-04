from collections import Counter

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people_count = Counter(people)

        boats = 0

        if people_count[limit]:
            # print(f"{people_count}")
            boats += people_count[limit]
            # print(f"boat #{boats} ({limit}) * {people_count[limit]}")
            del people_count[limit]
        
        changed = set()
        for P, countP in people_count.items():
            Q = limit - P
            countQ = people_count[Q]
            if countQ:
                if P == Q:
                    x = countP // 2
                else:
                    x = min(countP, countQ)
                if x:
                    boats += x
                    people_count[P] -= x
                    changed.add(P)
                    people_count[Q] -= x
                    changed.add(Q)
                    # print(f"boat #{boats} ({P}, {Q}) * {x}")
        for C in changed:
            if people_count[C] == 0:
                del people_count[C]

        while people_count:
            # print(f"{people_count}")
            mp = max(people_count)
            mp_count = people_count[mp]

            others = list([
                P
                for P in people_count.keys()
                if P + mp <= limit
            ])
            if others and mp_count:
                mo = max(others)
                if mp == mo:
                    x = mp_count // 2
                    # print(f"{mp} == {mo}: {x}")
                    if mp_count == 1:
                        other_others = list([
                            P
                            for P in others
                            if P < mp
                        ])
                        if other_others:
                            mo = max(other_others)
                            mo_count = people_count[mo]
                            x = min(mp_count, mo_count)
                        else:
                            x = 0
                        # print(f"OO={other_others} {mp=} {mo=} {x=}")
                else:
                    mo_count = people_count[mo]
                    x = min(mp_count, mo_count)

                if x:
                    boats += x
                    people_count[mp] -= x
                    if people_count[mp] == 0:
                        del people_count[mp]
                    people_count[mo] -= x
                    if people_count[mo] == 0:
                        del people_count[mo]
                    # print(f"boat #{boats} ({mp}, {mo}) * {x}")
                    continue

            x = mp_count
            boats += x
            people_count[mp] -= x
            if people_count[mp] == 0:
                del people_count[mp]
            # print(f"boat #{boats} ({mp}, -) * {x}")

        return boats

