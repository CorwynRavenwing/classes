class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:

        grid_H = len(board)
        grid_W = len(board[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < grid_H) and (0 <= Y < grid_W)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        def valueAt(cell: Tuple[int,int]) -> str:
            nonlocal board
            if OOB(cell):
                return 'X'
            (X, Y) = cell
            return board[X][Y]
        
        def nextCell(cell: Tuple[int,int], direction: Tuple[int,int]) -> Tuple[int,int]:
            (X, Y) = cell
            (I, J) = direction
            return (X + I, Y + J)
        
        def opponent(color: str) -> str:
            if color == 'W':
                return 'B'
            elif color == 'B':
                return 'W'
            else:
                print(f'ERROR: invalid {color=}')
                return None

        def isGoodLine(cell: Tuple[int,int], direction: Tuple[int,int], color: str) -> bool:
            print(f'isGoodLine({cell},{direction},{color}):')
            otherColor = opponent(color)
            cell = nextCell(cell, direction)
            value = valueAt(cell)
            # print(f'  {cell=} {value=}')
            if value != otherColor:
                print(f'  NO: Second cell is {value}, not {otherColor}')
                return False
            while (value := valueAt(cell)) == otherColor:
                print(f'  {cell=} {value=}')
                cell = nextCell(cell, direction)
            print(f'  {cell=} {value=}')
            if value != color:
                print(f'  NO: Last cell is {value}, not {otherColor}')
                return False
            print(f'  YES: test succeeded')
            return True
            
        directions = tuple([
            (I, J)
            for I in (-1, 0, +1)
            for J in (-1, 0, +1)
            if (I, J) != (0, 0)
        ])
        print(f'{directions=}')

        origin = (rMove, cMove)
        answers = [
            isGoodLine(origin, direction, color)
            for direction in directions
        ]
        print(f'{answers=}')
        return any(answers)

