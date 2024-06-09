class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        size_m = len(board)
        size_n = len(board[0])

        def printBoard() -> None:
            nonlocal board, size_n
            print('=' * size_n)
            for row in board:
                print(''.join(row))
            print('=' * size_n)
            return
        
        def getBoardVal(pos: List[int]) -> str:
            nonlocal board
            (posR, posC) = pos
            return board[posR][posC]

        def setBoardVal(pos: List[int], val: str) -> None:
            nonlocal board
            (posR, posC) = pos
            board[posR][posC] = val
            return
        
        def legalPos(pos: List[int]) -> bool:
            nonlocal size_m, size_n
            (R, C) = pos
            return ((0 <= R < size_m) and (0 <= C < size_n))

        def neighborsOf(pos: List[int]) -> List[List[int]]:
            (R, C) = pos
            directions = [
                (x, y)
                for x in [-1, 0, 1]
                for y in [-1, 0, 1]
            ]
            # print(f'{directions=}')
            adjacent = [
                (R+x, C+y)
                for (x, y) in directions
                if (x, y) != (0, 0)
            ]
            # print(f'{adjacent=}')
            neighbors = [
                pos
                for pos in adjacent
                if legalPos(pos)
            ]
            # print(f'{neighbors=}')
            return neighbors

        printBoard()

        found = getBoardVal(click)
        print(f'{click=} {found=}')
        if found == 'M':
            print(f'  BOOM!')
            setBoardVal(click, 'X')
            printBoard()
            return board
        
        to_reveal = [click]
        while to_reveal:
            position = to_reveal.pop()
            neighbors = neighborsOf(position)
            # print(f'{neighbors=}')
            mines = 0
            E_group = []
            for N in neighbors:
                value = getBoardVal(N)
                # print(f'  {N=} {value=}', end='')
                if value == 'M':
                    # print(f' ... mine')
                    mines += 1
                elif value == 'E':
                    if N not in to_reveal:
                        # print(f' ... E')
                        E_group.append(N)
                    # else:
                    #     print(f' ... E DUP!')
                # else:
                #     print(f' ... other')
            if mines:
                setBoardVal(position, str(mines))
            else:
                setBoardVal(position, 'B')
                to_reveal.extend(E_group)
            # printBoard()

        printBoard()
        return board

