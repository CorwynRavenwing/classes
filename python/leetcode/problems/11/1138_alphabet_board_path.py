class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        grid = (
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'uvwxy',
            'z****',
        )

        M = len(grid)
        N = len(grid[0])

        def getValue(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return all([
                (0 <= X < M),
                (0 <= Y < N),
                # special case: value "*" is OOB
                (getValue(cell) != '*'),
            ])

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
        @cache
        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            Neighbors = (
                (X + I, Y + J)
                for (I, J) in directions
            )
            return tuple([
                C
                for C in Neighbors
                if legalPos(C)
            ])

        coordinatesOfLetter = {
            getValue((X, Y)): (X, Y)
            for X in range(M)
            for Y in range(N)
        }

        directionsCmds = {
            'U': (-1, 0),
            'D': (+1, 0),
            'L': (0, -1),
            'R': (0, +1),
        }

        cursor = (0, 0)

        @cache
        def distanceBetween(cell1: Tuple[int,int], cell2: Tuple[int,int]) -> int:
            (X1, Y1) = cell1
            (X2, Y2) = cell2
            return sum([
                abs(X1 - X2),
                abs(Y1 - Y2),
            ])

        def moveOnceTowards(cell: Tuple[int,int]) -> str:
            nonlocal cursor
            (X, Y) = cursor
            currentDistance = distanceBetween(cursor, cell)
            # print(f'  once(): {cursor} -> {cell} ({currentDistance})')

            for (dir, (I, J)) in directionsCmds.items():
                neighbor = (X + I, Y + J)
                nDist = distanceBetween(neighbor, cell)
                # print(f'    {dir}: {neighbor} ({nDist})')
                if OOB(neighbor):
                    # print(f'      -> OOB')
                    continue
                if nDist > currentDistance:
                    # print(f'      -> wrong way')
                    continue
                cursor = neighbor
                # print(f'      -> yes ({cursor})')
                return dir
            
            raise Exception(f'Error: no legal moves toward target found')
        
        def moveTo(letter: str) -> str:
            nonlocal cursor
            cell = coordinatesOfLetter[letter]
            print(f'moveTo("{letter}"): {cursor} -> {cell}')
            moves = []
            while cursor != cell:
                moves.append(
                    moveOnceTowards(cell)
                )
            return ''.join(moves)
        
        answer = ''
        for letter in target:
            answer += moveTo(letter)
            answer += '!'
        
        return answer

# NOTE: Runtime 43 ms Beats 21.74%
# NOTE: Memory 16.80 MB Beats 9.43%
