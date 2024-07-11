class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        seatGroupsBlocked = {
            1: '',
            2: 'A',
            3: 'A',
            4: 'AB',
            5: 'AB',
            6: 'BC',
            7: 'BC',
            8: 'C',
            9: 'C',
            10: '',
        }
        familiesByBlockedGroups = {
            (): 2,              # A + C
            ('A',): 1,          # B or C
            ('B',): 2,          # A + C
            ('C',): 1,          # A or B
            ('A', 'B'): 1,      # C
            ('A', 'C'): 1,      # B
            ('B', 'C'): 1,      # A
            ('A', 'B', 'C'): 0, # none
        }
        # print(f'{familiesByBlockedGroups=}')
        reservedByRow = {}
        for (row, seat) in reservedSeats:
            reservedByRow.setdefault(row, [])
            reservedByRow[row].append(seatGroupsBlocked[seat])
        # print(f'{reservedByRow=}')
        # re-create this dict as a tuple of unique letters
        reservedByRow = {
            row: tuple(sorted(set([
                G
                for group in blockedGroups
                for G in group
            ])))
            for row, blockedGroups in reservedByRow.items()
        }
        print(f'{reservedByRow=}')
        nonReservedRows = n - len(reservedByRow)
        print(f'2 families in each of {nonReservedRows} rows')
        answer = 2 * nonReservedRows
        for row, blockedGroups in reservedByRow.items():
            F = familiesByBlockedGroups[blockedGroups]
            print(f'{row=} {F}: {blockedGroups}')
            answer += F

        return answer

