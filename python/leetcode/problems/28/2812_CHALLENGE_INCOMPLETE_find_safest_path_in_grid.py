class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)
        assert n == len(grid[0])

        thieves = [
            (x, y)
            for x, row in enumerate(grid)
            for y, val in enumerate(row)
            if val == 1
        ]
        print(f'{thieves[:10]=}')

        def manhattan_distance(P1, P2):
            (a, b) = P1
            (x, y) = P2
            return (abs(a - x) + abs(b - y))
        
        def safeness_of_cell(P):
            nonlocal thieves
            distances = [
                manhattan_distance(P, T)
                for T in thieves
            ]
            answer = min(distances)
            # print(f'SOC({P}): {distances=} {answer=}')
            return answer
        
        def is_legal(P):
            nonlocal n
            (x, y) = P
            return (
                (0 <= x < n) and (0 <= y < n)
            )

        def neighbors_of(P):
            (x, y) = P
            neighbors = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1),
            ]
            neighbors = [
                P
                for P in neighbors
                if is_legal(P)
            ]
            return list(neighbors)

        # def neighbors_of_any(points):
        #     neighbors = [
        #         N
        #         for P in points
        #         for N in neighbors_of(P)
        #     ]
        #     return list(set(neighbors))
        
        safeness = {
            (x, y): safeness_of_cell((x, y))
            for x, row in enumerate(grid)
            for y in range(len(row))
        }
        # print(f'{safeness=}')

        origin = (0, 0)
        target = (n-1, n-1)
        print(f'{target=} area={n*n}')
        known_safeness = {}
        to_check = [(safeness[origin], origin)]
        while to_check:
            print(f'L={len(to_check)}')
            to_check.sort()
            check = to_check.pop()  # highest score, then lower-rightest location
            (current_score, W) = check
            print(f'  score={current_score} {W=}')
            if W not in known_safeness:
                known_safeness[W] = current_score
            elif known_safeness[W] != current_score:
                print(f'    KS[{W}]={known_safeness[W]} <> CS={current_score}')
                continue
            if W == target:
                print(f'QUITTING EARLY: {W=}')
                return known_safeness[target]
            neighbors = neighbors_of(W)
            for N in neighbors:
                if N in known_safeness:
                    # print(f'    skip ({known_safeness[N]}, {N})')
                    continue
                C = (min(current_score, safeness[N]), N)
                if C not in to_check:
                    # print(f'    ADD  {C}')
                    to_check.append(C)
                # else:
                #     print(f'    dup  {C}')

        return known_safeness[target]

# TODO: timing out for large data sets

