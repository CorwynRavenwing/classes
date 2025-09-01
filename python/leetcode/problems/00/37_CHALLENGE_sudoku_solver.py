class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        NINE = range(1, 10)
        ROW = lambda R: f'R{R}'
        COL = lambda C: f'C{C}'
        BOX = lambda B: f'B{B}'
        BOX_NUM = lambda R, C: (
            ((R - 1) // 3) * 3 + ((C - 1) // 3) + 1
        )
        CELL = lambda R, C: f'({R},{C})'
        ALL_VALUES = lambda: set('123456789')

        PICK = lambda S: next(iter(S))
        
        UNKNOWN = 'unknown'
        SINGLE = 'single'
        ERROR = 'single'
        
        group_cells = {}
        for i in NINE:
            group_cells.setdefault(ROW(i), [])
            group_cells.setdefault(COL(i), [])
            group_cells.setdefault(BOX(i), [])
        
        constraints = {}
        cell_groups = {}
        constraints.setdefault(UNKNOWN, set())
        constraints.setdefault(SINGLE, set())
        constraints.setdefault(ERROR, '')
        for i in NINE:
            row = ROW(i)
            for j in NINE:
                col = COL(j)
                cell = CELL(i, j)
                constraints[cell] = ALL_VALUES()
                box_num = BOX_NUM(i, j)
                box = BOX(box_num)
                # print(f'DEBUG: {cell=} in {box_num=}')
                group_cells[row].append(cell)
                group_cells[col].append(cell)
                group_cells[box].append(cell)
                constraints[UNKNOWN].add(cell)
                cell_groups[cell] = (row, col, box)

        # print(f'{constraints=}')
        # print(f'{group_cells=}')
        # print(f'{cell_groups=}')

        def copy_constraints(input_constraints: Dict[str,Set[str]]) -> Dict[str,Set[str]]:
            output_constraints = {
                label: input_set.copy()
                for label, input_set in input_constraints.items()
            }
            return output_constraints

        def update_cell_yes_only(constraints: Dict[str,Set[str]], cell: str, value: str) -> bool:
            unknown = constraints[UNKNOWN]
            if cell not in unknown:
                constraints[ERROR] = f'Error: update_cell_yes_only() {cell=} not in {unknown=}'
                print(f'DEBUG: [A] set {constraints[ERROR]=}')
                return False
            possible = constraints[cell]
            if value not in possible:
                constraints[ERROR] = f'Error: update_cell_yes_only() {value=} not in {possible=}'
                print(f'DEBUG: [B] set {constraints[ERROR]=}')
                return False
            constraints[cell] = set(value)
            constraints[UNKNOWN].remove(cell)
            constraints[SINGLE].add(cell)
            print(f'  {cell} = {value}')
            # print(f'DEBUG: set {constraints[SINGLE]=}')
            return True
        
        def update_cell_no_only(constraints: Dict[str,Set[str]], cell: str, value: str) -> bool:
            constraints[cell].remove(value)
            remaining = len(constraints[cell])
            if remaining == 1:
                print(f'    {cell} is now a single ={value}')
                constraints[UNKNOWN].remove(cell)
                constraints[SINGLE].add(cell)
            elif remaining == 0:
                constraints[ERROR] = f'Error: update_cell_no_only() {cell=} can no longer be anything: {constraints[cell]=}'
                print(f'DEBUG: [C] set {constraints[ERROR]=}')
                return False
            return True
        
        def propagate_singles(constraints: Dict[str,Set[str]]) -> bool:
            # print(f'\nPropagating singles:')

            while constraints[SINGLE]:
                # print(f'---------------')
                cell = constraints[SINGLE].pop()
                value = PICK(constraints[cell])
                for group in cell_groups[cell]:

                    for neighbor in group_cells[group]:
                        if neighbor == cell:
                            continue
                        if value not in constraints[neighbor]:
                            continue
                        # print(f'  {cell}+{group} = {neighbor}')
                        if not update_cell_no_only(constraints, neighbor, value):
                            return False
            return True

        def copy_update_cell_yes_and_propagate(input_constraints: Dict[str,Set[str]], cell: str, value: str) -> Dict[str,Set[str]]:

            output_constraints = copy_constraints(input_constraints)

            if update_cell_yes_only(output_constraints, cell, value):
                _ = propagate_singles(output_constraints)

            return output_constraints
        
        def copy_update_cell_no_and_propagate(input_constraints: Dict[str,Set[str]], cell: str, value: str) -> Dict[str,Set[str]]:

            output_constraints = copy_constraints(input_constraints)

            if update_cell_no_only(output_constraints, cell, value):
                _ = propagate_singles(output_constraints)

            return output_constraints
            
        knowns = [
            (CELL(i + 1, j + 1), value)
            for i, row in enumerate(board)
            for j, value in enumerate(row)
            if value != '.'
        ]
        # print(f'{knowns=}')

        print(f'Setting knowns:')

        for cell, value in knowns:
            if not update_cell_yes_only(constraints, cell, value):
                print(f'ERROR [1]: {constraints[ERROR]}')
                print(f'Error in loading knowns: IMPOSSIBLE')
                return

        # print(f'{constraints[UNKNOWN]=}')
        # print(f'{constraints[SINGLE]=}')

        if not propagate_singles(constraints):
            print(f'ERROR [2]: {constraints[ERROR]}')
            print(f'Error in propagating knowns: IMPOSSIBLE')
            return
        
        # print(f'{constraints[UNKNOWN]=}')
        # print(f'{constraints[SINGLE]=}')

        print(f'\nGuessing:')
        stack = []
        while constraints[UNKNOWN]:
            unknown = constraints[UNKNOWN]
            print(f'STACK: {len(stack)}\tUNKNOWN: {len(unknown)}')
            cell = PICK(unknown)
            possibles = constraints[cell]
            print(f'  {cell} = {possibles}')
            value = PICK(possibles)
            print(f'\nGUESS {cell} = {value}')

            constraints_no = copy_update_cell_no_and_propagate(constraints, cell, value)
            if constraints_no[ERROR]:
                print(f'  Guessing NO fails')
                pass
            else:
                print(f'  putting NO guess on the stack')
                stack.append(constraints_no)

            constraints_yes = copy_update_cell_yes_and_propagate(constraints, cell, value)
            if constraints_yes[ERROR]:
                print(f'  Guessing YES fails: popping NO guess from stack')
                constraints = stack.pop(-1)
            else:
                print(f'  Guessing YES: loop again')
                constraints = constraints_yes
        
        print(f'\nSetting return values:')

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if value == '.':
                    cell = CELL(i + 1, j + 1)
                    possibles = constraints[cell]
                    assert len(possibles) == 1
                    value = PICK(possibles)
                    print(f'  {cell} = {value}')
                    board[i][j] = value

        """
        Do not return anything, modify board in-place instead.
        """
        
        pass
        
# NOTE: Acceptance Rate 64.9% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (several edge cases)
# NOTE: Runtime 635 ms Beats 83.82%
# NOTE: Memory 18.59 MB Beats 6.58%
