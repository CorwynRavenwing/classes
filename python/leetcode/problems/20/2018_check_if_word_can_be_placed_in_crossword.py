class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:

        def processRow(row: List[str]) -> List[str]:
            blocking = ''.join(row).replace(' ', '_')
            # print(f'{blocking=}')
            groups = blocking.split('#')
            # print(f'{groups=}')
            return [
                G
                for G in groups
                if G
            ]

        def processRows(board: List[List[str]]) -> List[str]:
            return [
                obj
                for row in board
                for obj in processRow(row)
            ]

        def processBoth(board: List[List[str]]) -> List[str]:
            print(f'Process rows:')
            possiblesRow = processRows(board)
            print(f'Process columns:')
            possiblesCol = processRows(zip(*board))
            return possiblesRow + possiblesCol

        def match(word: str, space: str) -> bool:
            if len(word) != len(space):
                return False
            print(f'match("{word}","{space}"):')
            for (A, B) in zip(word, space):
                if B not in ['_', A]:
                    print(f'  mismatch {A},{B}')
                    return False
            return True
        
        possibles = processBoth(board)
        print(f'{possibles=}')

        for P in possibles:
            if match(word, P):
                print(f'Yes!  Fit {word=} into space "{P}"')
                return True
            reversedP = ''.join(
                reversed(P)
            )
            if P != reversedP:
                if match(word, reversedP):
                    print(f'Yes!  Fit {word=} into space "{P}", backwards')
                    return True
        print(f'No.  Cannot fit {word=} anywhere.')
        return False

