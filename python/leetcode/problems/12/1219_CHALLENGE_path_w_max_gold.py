class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        cells_with_gold = [
            (x, y)
            for x, row in enumerate(grid)
            for y, G in enumerate(row)
            if G > 0
        ]
        print(f'{cells_with_gold=}')
        if not cells_with_gold:
            return 0
        
        all_gold = sum([
            G
            for row in grid
            for G in row
        ])

        def neighbors(point: Tuple[int,int]) -> List[Tuple[int,int]]:
            (x, y) = point
            answer = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1),
            ]
            answer = [
                N
                for N in answer
                if N in cells_with_gold
            ]
            return list(answer)

        # for each cell with gold, collect it, and create a path of just that one point
        to_check = [
            (grid[x][y], [(x, y)])
            for (x, y) in cells_with_gold
        ]

        answers = []
        while to_check:
            to_check.sort(reverse=True)
            print(f'L={len(to_check)}')
            check = to_check.pop(0)
            # print(f'  {check=}')
            (gold_so_far, path_so_far) = check
            # print(f'  gold={gold_so_far} path=[{path_so_far[0]} ... {path_so_far[-1]}] (len={len(path_so_far)})')
            point = path_so_far[-1]
            next_points = neighbors(point)
            next_points = list([
                P
                for P in next_points
                if P not in path_so_far
            ])
            # print(f'    {next_points=}')
            if not next_points:
                # print(f'    No next points: stopping')
                if gold_so_far == all_gold:
                    print("got all the gold!  stopping")
                    print(f'  path = {path_so_far}')
                    return all_gold
                answers.append(check)
                continue
            for (x, y) in next_points:
                this_gold = grid[x][y]
                C = (
                    gold_so_far + this_gold,
                    path_so_far + [(x, y)],
                )
                # print(f'      +{this_gold} {C=}')
                to_check.append(C)
        answers.sort(reverse=True)
        # print(f'{answers=}')
        winner = answers[0]
        (gold, path) = winner
        print(f'{gold=}')
        print(f'{path=}')
        return gold

