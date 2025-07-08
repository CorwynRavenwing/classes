class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        
        def legalKnightsMove(pos1: Tuple[int,int], pos2: Tuple[int,int]) -> bool:
            (X, Y) = pos1
            possible = (
                (X - 2, Y - 1), (X - 2, Y + 1),
                (X + 2, Y - 1), (X + 2, Y + 1),
                (X - 1, Y - 2), (X - 1, Y + 2),
                (X + 1, Y - 2), (X + 1, Y + 2),
            )
            # print(f'DEBUG: {pos1} -> {possible}')
            return pos2 in possible

        positions = [
            (value, (X, Y))
            for X, row in enumerate(grid)
            for Y, value in enumerate(row)
        ]
        positions.sort()
        print(f'{positions=}')
        squares = len(positions)
        print(f'{squares=}')
        firstpos = positions[0][1]
        origin = (0, 0)
        if firstpos != origin:
            print(f'{firstpos=} should be {origin}!')
            return False
        firstmove = positions[0][0]
        if firstmove != 0:
            print(f'{firstmove=} should be zero!')
            return False
        lastmove = positions[-1][0]
        if lastmove != squares - 1:
            print(f'{lastmove=} should be {squares-1=}!')
            return False
        print(f'{positions[0]}')
        for P1, P2 in pairwise(positions):
            M1, pos1 = P1
            M2, pos2 = P2
            if M1 + 1 != M2:
                print(f'{M1+1=} should be {M2=}!')
                return False
            if legalKnightsMove(pos1, pos2):
                print(f'{P2}')
                continue
            print(f'{P2} UNREACHABLE')
            return False
        print(f'Done')
        return True

# NOTE: Acceptance Rate 58.0% (medium)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (edge case with first pos not 0,0)
# NOTE: Runtime 12 ms Beats 5.94%
# NOTE: Memory 17.75 MB Beats 70.79%
