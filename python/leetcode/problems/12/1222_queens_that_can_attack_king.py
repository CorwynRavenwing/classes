class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        M = 8
        N = 8

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, -1), (-1, +0), (-1, +1),
            (+0, -1), (+0, +0), (+0, +1),
            (+1, -1), (+1, +0), (+1, +1),
        )

        def move(cell: Tuple[int,int], dir: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = cell
            (I, J) = dir
            return (X + I, Y + J)
        
        king = tuple(king)
        print(f'{king=}')
        queens = set(map(tuple, queens))
        print(f'{queens=}')

        answer = []
        for dir in directions:
            if dir == (0, 0):
                continue
            cursor = king
            print(f'\n{dir=} {cursor=}')
            while legalPos(cursor := move(cursor, dir)):
                print(f'{dir=} {cursor=}')
                if cursor in queens:
                    print(f'  Found')
                    answer.append(cursor)
                    break

        return answer

# NOTE: Accepted on second Run (first was sign typo)
# NOTE: Accepted on first Submit
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.73 MB Beats 17.03%
