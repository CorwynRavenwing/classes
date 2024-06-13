class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:

        def in_bounds(x, y, arm):
            nonlocal n
            return (
                (
                    (0 <= (x - arm) <= (x + arm) < n)
                ) and (
                    (0 <= (y - arm) <= (y + arm) < n)
                )
            )
        
        max_size = (n // 2) + 1
        if ((max_size - 1) * 2 + 1) > n:
            print(f'{max_size=} wont fit')
            max_size -= 1
        print(f'{max_size=}')
        xmines = {}
        ymines = {}
        for (mX, mY) in mines:
            xmines.setdefault(mX, [])
            xmines[mX].append(mY)

            ymines.setdefault(mY, [])
            ymines[mY].append(mX)

        answer = 0
        print(f'x: range {0}..{n-1}')
        for x in range(0, n):
            nearest_wall_x = min([
                x,
                (n - x - 1),
            ]) + 1
            # print(f'  {nearest_wall_x=}')
            if nearest_wall_x <= answer:
                continue
            # print(f'y: range {1}..{n-1}')
            for y in range(0, n):
                # print(f'{x},{y}:')
                nearest_wall_x = min([
                    x,
                    (n - x - 1),
                ]) + 1
                # print(f'  {nearest_wall_x=}')
                if nearest_wall_x <= answer:
                    break
                nearest_wall_y = min([
                    y,
                    (n - y - 1),
                ]) + 1
                # print(f'  {nearest_wall_y=}')
                if nearest_wall_y <= answer:
                    continue
                nearest_wall = min(nearest_wall_x, nearest_wall_y)
                if x in xmines:
                    if y in xmines[x]:
                        # found a mine
                        continue
                # print(f'size range {1}..{nearest_wall}')

                for size in range(1, nearest_wall+1):
                    # print(f'  {size=}')
                    arm = size - 1
                    if in_bounds(x, y, arm):
                        # print(f'    {arm=}')
                        if x in xmines:
                            if y-arm in xmines[x]:
                                # found a mine
                                size -= 1
                                break
                            if y+arm in xmines[x]:
                                # found a mine
                                size -= 1
                                break
                        if y in ymines:
                            if x-arm in ymines[y]:
                                # found a mine
                                size -= 1
                                break
                            if x+arm in ymines[y]:
                                # found a mine
                                size -= 1
                                break
                    else:
                        print(f'({x},{y}) OOB! ({x-size},{y-size}) ({x+size},{y+size})')
                        size -= 1
                        break
                if answer < size:
                    print(f'({x},{y}) +{size}')
                answer = max(answer, size)
                continue
        return answer

