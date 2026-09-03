class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        # variable rename
        grid = classroom

        # GRID FUNCTIONS

        M = len(grid)
        N = len(grid[0])

        def legalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < M) and (0 <= Y < N)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not legalPos(cell)

        directions = (
            (-1, 0),
            (+1, 0),
            (0, -1),
            (0, +1),
        )
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

        def getValue(cell: Tuple[int,int]) -> int:
            (X, Y) = cell
            return grid[X][Y]

        def setValue(cell: Tuple[int,int], value: int) -> bool:
            (X, Y) = cell
            if OOB(cell):
                return False
            grid[X][Y] = value
            return True

        def allCellsWithValue(value: int) -> List[Tuple[int,int]]:
            return [
                (X, Y)
                for X in range(M)
                for Y in range(N)
                if getValue((X, Y)) == value
            ]

        def allValues() -> Set[Tuple[int,int]]:
            return {
                V
                for row in grid
                for V in row
            }

        # GRID POSTION VALUES

        startList = allCellsWithValue('S')
        resetList = allCellsWithValue('R')
        trashList = allCellsWithValue('L')
        # blockList = allCellsWithValue('X')
        origin = startList.pop()
        assert not startList
        # print(f'{origin=}')
        # print(f'{resetList=}')
        # print(f'{trashList=}')
        # print(f'{blockList=}')

        # BITMASK FUNCTIONS

        def set_bit(value: int, bit: int) -> int:
            mask = 1 << bit
            return value | mask
        
        def check_bit(value, bit) -> bool:
            mask = 1 << bit
            return value & mask
        
        trashes = len(trashList)
        # print(f'{trashes=}')
        
        all_mask = (1 << trashes) - 1
        # print(f'{all_mask=}')
        # for bit in range(10):
        #     # print(f'{check_bit(all_mask, bit)=}')

        best_energy = {}
        answers = []
        queue = [(origin, 0, energy, 0)]
        # append to right, take from left -> BFS
        while queue:
            # print(f'Q={len(queue)}')
            state = queue.pop(0)
            # print(f'  {state}')
            (pos, mask, e, moves) = state
            
            value = getValue(pos)
            if value == 'X':
                # print(f'  NO, X')
                continue
            if value == 'R':
                # print(f'  recharge: e={e}->{energy}')
                e = energy

            loc = (pos, mask)
            best = best_energy.get(loc, -1)
            if best > e:
                # print(f'  NO, already seen e={best}')
                continue
            else:
                best_energy[loc] = e
            
            new_mask = mask
            if value == 'L':
                trashID = trashList.index(pos)
                new_mask = set_bit(mask, trashID)
                changed = (new_mask != mask)
                flag = ("NEW" if changed else "dup")
                # print(f'  L={trashID} mask={mask}->{new_mask} {flag}')
            
            if new_mask == all_mask:
                # print(f'  ANSWER {moves=}')
                answers.append(moves)
                continue
            
            if e <= 0:
                # print(f'  STOP, out of energy')
                continue
            # else:
                # print(f'  Neighbors:')
            
            # if moves > 10:
            #     # print(f'  STOP, {moves=}')
            #     continue
            
            for neighbor in neighborsOf(pos):
                state = (neighbor, new_mask, e - 1, moves + 1)
                # print(f'    -> {state}')
                queue.append(state)
        
        # print(f'{answers=}')

        return min(answers, default=-1)

# NOTE: Acceptance Rate 28.8% (medium)

# NOTE: INCOMPLETE, TLE
