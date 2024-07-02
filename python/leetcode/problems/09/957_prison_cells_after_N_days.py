class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        def transform(input: List[int]) -> List[int]:
            retval = [None] * len(input)
            retval[0] = 0   # these two cells
            retval[-1] = 0  # don't have 2 neighbors
            for i in range(1, len(input) - 1):
                L = input[i - 1]
                R = input[i + 1]
                C = (1 if (L == R) else 0)
                # print(f'{i=} [{L},{R}] -> {C}')
                retval[i] = C
            return tuple(retval)
        
        seen_when = {}
        cells_then = {}
        print(f'Day {0}: {cells}')
        for day in range(1, n + 1):
            cells = transform(cells)
            if cells in seen_when:
                label = f"same as #{seen_when[cells]}"
                compare = ((day - 1) % 14) + 1
            else:
                label = ""
                compare = ""
            if day <= 30:
                seen_when[cells] = day
                cells_then[day] = cells
            print(f'Day {day}: {cells} {label} ~{compare}')
            
            if day == n:
                print(f'return early')
                return cells
            
            if day >= 30:
                break
        
        compare = ((n - 1) % 14) + 1
        label = f"same as #{compare}"
        cells = cells_then[compare]
        print(f'Day {n}: {cells} {label}')

        return cells

