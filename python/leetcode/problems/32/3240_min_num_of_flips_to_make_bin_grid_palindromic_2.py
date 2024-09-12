class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        # we borrow some code from #3239:

        M = len(grid)
        N = len(grid[0])

        def centerObject(thing: List[any]) -> any:
            if thing is None:
                return None
            Len = len(thing)
            even = (Len % 2 == 0)
            if even:
                return None
            Half = Len // 2
            # print(f'{Len=} {even=} {Half=}')
            centerObj = thing[Half]
            return centerObj

        def centerCell(grid: List[List[int]]) -> int:
            centerRow = centerObject(grid)
            centerCell = centerObject(centerRow)
            return centerCell

        def rowPairs(row: List[int]) -> int:
            Len = len(row)
            Half = Len // 2
            firstHalf = row[:Half]
            lastHalf = row[Half:]
            lastRev = tuple(reversed(tuple(lastHalf)))
            return [
                (A, B)
                for (A, B) in zip(firstHalf, lastRev)
            ]

        def centerRowPairs(grid: List[List[int]]) -> List[Tuple[int,int]]:
            centerRow = centerObject(grid)
            if centerRow is None:
                return []
            return rowPairs(centerRow)
        
        def centerRowsBothWays(grid: List[List[int]]) -> List[Tuple[int,int]]:
            return (
                (
                    centerRowPairs(grid)
                ) + (
                    centerRowPairs(tuple(zip(*grid)))
                )
            )

        def cornerGroups(grid: List[List[int]]) -> List[Tuple[int,int,int,int]]:
            cornerCoords = [
                (
                    # trusing Hint 1 to be accurate:
                    (X, Y),
                    (M - 1 - X, Y),
                    (M - 1 - X, N - 1 - Y),
                    (X, N - 1 - Y),
                )
                # only do X, Y for the upper-left quadrant
                for X in range(M // 2)
                for Y in range(N // 2) 
            ]
            corners = [
                tuple([
                    grid[X][Y]
                    for (X, Y) in coordGroup
                ])
                for coordGroup in cornerCoords
            ]
            return [
                (A, B, C, D)
                for (A, B, C, D) in corners
                if not (A == B == C == D)
            ]

        corners = cornerGroups(grid)
        print(f'{corners=}')
        corner_sums = tuple(map(sum, corners))
        print(f'{corner_sums=}')
        corner_changes = [
            min([
                S,
                (4 - S) % 4,
            ])
            for S in corner_sums
        ]
        print(f'{corner_changes=}')
        corner_change_count = sum(corner_changes)
        print(f'{corner_change_count=}')

        middles = centerRowsBothWays(grid)
        print(f'{middles=}')
        middle_sums = tuple(map(sum, middles))
        print(f'{middle_sums=}')
        middle_changes = [
            min([
                S,
                (2 - S) % 2,
            ])
            for S in middle_sums
        ]
        print(f'{middle_changes=}')
        middle_change_count = sum(middle_changes)
        print(f'{middle_change_count=}')
        middle_grand_total = sum(middle_sums)
        print(f'{middle_grand_total=}')
        middle_parity_fix = sum([
            min([
                S % 4,
                (4 - S) % 4,
            ])
            for S in [middle_grand_total]   # yes, a loop of one object
        ])
        print(f'{middle_parity_fix=}')

        center = centerCell(grid)
        print(f'{center=}')
        if center is None:
            center = 0
        
        answer = 0
        if center:
            print(f'{1}: Must clear center')
            answer += center
        
        if corner_change_count:
            print(f'{corner_change_count}: Corner changes')
            answer += corner_change_count
        
        if middle_change_count:
            print(f'{middle_change_count}: Middle changes')
            answer += middle_change_count
            
        if middle_parity_fix:
            print(f'{middle_parity_fix}: Middle parity fix')
            if middle_parity_fix <= 2 * middle_change_count:
                print(f'  (included in Middle changes)')
            else:
                leftover_parity_fix = middle_parity_fix - 2 * middle_change_count
                print(f'  ({leftover_parity_fix} not included in Middle changes)')
                answer += leftover_parity_fix

        return answer

# NOTE: Runtime 2960 ms Beats 8.57%
# NOTE: Memory 71.02 MB Beats 24.56%
