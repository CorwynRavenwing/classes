class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:

        M = len(image)
        N = len(image[0])

        INV = lambda x: tuple(zip(*x))

        # given a list of 3 values, return a list of 2 booleans
        def INT3_TO_BOOL2(row: List[int]) -> List[bool]:
            answer = tuple([
                abs(A - B) <= threshold
                for (A, B) in pairwise(row)
            ])
            # print(f'INT3_TO_BOOL2({row}) -> {answer}')
            return answer
        
        # given a list of N booleans, return a list of N-1 booleans
        def BOOL_TO_BOOL_MINUS(ab: List[bool]) -> List[bool]:
            answer = tuple([
                A and B
                for (A, B) in pairwise(
                    ab
                )
            ])
            # print(f'BOOL_TO_BOOL_MINUS({ab}) -> {answer}')
            return answer

        # given a list of N booleans, return a list of N+1 booleans
        def BOOL_TO_BOOL_PLUS(ab: List[bool]) -> List[bool]:
            answer = BOOL_TO_BOOL_MINUS(
                (False,) + tuple(ab) + (False,)
            )
            # print(f'BOOL_TO_BOOL_PLUS({ab}) -> {answer}')
            return answer

        # given a 3x3 grid of values, return a 3x2 grid of booleans
        INT33_TO_BOOL32 = lambda x: tuple(map(INT3_TO_BOOL2, x))
        # given a MxN grid of booleans, return a Mx(N-1) grid of booleans
        BOOL_TO_BOOL_MINUS_GRID = lambda x: tuple(map(BOOL_TO_BOOL_MINUS, x))
        # given a MxN grid of booleans, return a Mx(N+1) grid of booleans
        BOOL_TO_BOOL_PLUS_GRID = lambda x: tuple(map(BOOL_TO_BOOL_PLUS, x))
        
        # given two equal-sized grids of booleans, return a grid of cellwise "AND"
        def AND(gridA: List[List[bool]], gridB: List[List[bool]]) -> List[List[bool]]:
            return tuple([
                [
                    valA and valB
                    for valA, valB in zip(rowA, rowB)
                ]
                for rowA, rowB in zip(gridA, gridB)
            ])

        def INT33_TO_BOOL22(grid: List[List[int]]) -> List[List[bool]]:
            int33_to_bool22_half = lambda x: (
                BOOL_TO_BOOL_MINUS_GRID(
                    INV(
                        INT33_TO_BOOL32(x)
                    )
                )
            )
            BOOL22a = INV(int33_to_bool22_half(grid))  # INV last
            BOOL22b = int33_to_bool22_half(INV(grid))  # INV first
            return AND(BOOL22a,BOOL22b)
        
        def INT33_TO_BOOL33(grid: List[List[int]]) -> List[List[bool]]:
            bool22 = INT33_TO_BOOL22(grid)
            bool22_to_bool33_half = lambda x: (
                BOOL_TO_BOOL_PLUS_GRID(
                    INV(
                        BOOL_TO_BOOL_PLUS_GRID(x)
                    )
                )
            )
            BOOL33a = INV(bool22_to_bool33_half(bool22))    # INV last
            BOOL33b = bool22_to_bool33_half(INV(bool22))    # INV first
            return AND(BOOL33a,BOOL33b)

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        # def OOB(cell: Tuple[int,int]) -> bool:
        #     return not legalPos(cell)
        
        def valueAt(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return (
                image[X][Y]
                if legalPos(cell)
                else None
            )

        isCenterOfRegion = INT33_TO_BOOL33(image)
        # print(f'{isCenterOfRegion=}')

        directions = (
            (-1, -1), (-1, +0), (-1, +1),
            (+0, -1), (+0, +0), (+0, +1),
            (+1, -1), (+1, +0), (+1, +1),
        )
        def MembersOfRegion(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            return tuple([
                (X + I, Y + J)
                for (I, J) in directions
            ])
        Num = [[0 for j in range(N)] for i in range(M)]
        Sum = [[0 for j in range(N)] for i in range(M)]

        for i, row in enumerate(isCenterOfRegion):
            for j, val in enumerate(row):
                if not val:
                    continue
                # print(f'{(i,j)=}')
                region = MembersOfRegion((i, j))
                # print(f'  {region=}')
                values = tuple(map(valueAt, region))
                # print(f'  {values=}')
                average = sum(values) // len(values)
                # print(f'  {average=}')
                for (X, Y) in region:
                    # print(f'  {(X,Y)=}')
                    Num[X][Y] += 1
                    Sum[X][Y] += average
        print(f'{Num=}')
        print(f'{Sum=}')
        Avg = [
            [
                (
                    total // count
                    if count
                    else value
                )
                for count, total, value in zip(rowNum, rowSum, row)
            ]
            for rowNum, rowSum, row in zip(Num, Sum, image)
        ]
        # print(f'{Avg=}')
        return Avg
# NOTE: Runtime 5321 ms Beats 62.31%
# NOTE: Memory 40.64 MB Beats 57.69%
