class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:

        grid_H = len(grid)
        grid_W = len(grid[0])

        (lowestPrice, highestPrice) = pricing

        def isLegalPos(cell: Tuple[int,int]) -> bool:
            (X, Y) = cell
            return (0 <= X < grid_H) and (0 <= Y < grid_W)

        def OOB(cell: Tuple[int,int]) -> bool:
            return not isLegalPos(cell)
        
        directions = (
            (+1, 0),
            (-1, 0),
            (0, +1),
            (0, -1),
        )

        def neighborsOf(cell: Tuple[int,int]) -> List[Tuple[int,int]]:
            (X, Y) = cell
            return [
                (X + I, Y + J)
                for (I, J) in directions
            ]

        def valueAt(cell: Tuple[int,int]) -> int:
            if OOB(cell):
                return None
            else:
                (X, Y) = cell
                return grid[X][Y]

        # def setValueAt(cell: Tuple[int,int], value: int) -> None:
        #     if OOB(cell):
        #         return
        #     else:
        #         (X, Y) = cell
        #         grid[X][Y] = value
        #         return

        answers = []
        seen = set()
        queue = {(0, tuple(start))}
        while queue:
            newQ = set()
            # queue/newQ is so our search is breadth-first
            # which keeps our "distance" numbers accurate
            for (distance, cell) in queue:
                # print(f'{cell} d={distance}:')
                if cell in seen:
                    # print(f'  (seen)')
                    continue
                else:
                    seen.add(cell)
                
                V = valueAt(cell)
                if V > 1:
                    # print(f'  {V=}')
                    if lowestPrice <= V <= highestPrice:
                        answers.append(
                            (distance, V, cell)
                        )
                    # else:
                    #     print(f'    (Price OOB)')

                for N in neighborsOf(cell):
                    # print(f'    {N=}')
                    if N in seen:
                        # print(f'      (seen)')
                        continue
                    elif OOB(N):
                        # print(f'      (OOB)')
                        continue
                    else:
                        V = valueAt(N)
                        if V == 0:
                            # print(f'      (wall)')
                            continue
                        else:
                            # print(f'      (newQ)')
                            newQ.add(
                                (distance + 1, N)
                            )
            queue = newQ
        answers.sort()
        print(f'{answers=}')
        answerCells = [
            cell
            for distance, price, cell in answers
        ]
        return answerCells[:k]

