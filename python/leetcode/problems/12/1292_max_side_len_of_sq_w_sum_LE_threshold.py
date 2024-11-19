class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        grid_M = len(mat)
        grid_N = len(mat[0])

        gridPartials = tuple([
            (0,) + tuple(accumulate(row))
            for row in mat
        ])
        # print(f'{gridPartials=}')

        def test(target: int) -> bool:
            if target == 0:
                return True
            
            if target == 1:
                grid_min = min([
                    min(row)
                    for row in mat
                ])
                print(f'{grid_min=}')
                return (grid_min <= threshold)
            
            size = target - 1
            for X in range(grid_M):
                try:
                    check_row = mat[X + size][0]
                except IndexError:
                    break
                for Y in range(grid_N):
                    # print(f'{size=} (X,Y)=({X},{Y}):')
                    try:
                        check_column = mat[0][Y + size]
                    except IndexError:
                        break
                    total = 0
                    for offset in range(target):
                        rowPartial = gridPartials[X + offset]
                        # print(f'  {rowPartial=}')
                        thisRowTotal = rowPartial[Y + size + 1] - rowPartial[Y]
                        # print(f'  {thisRowTotal=} = rp[{Y}+{size}+1]={rowPartial[Y+size+1]} - rp[{Y}]={rowPartial[Y]}')
                        total += thisRowTotal
                        if total > threshold:
                            # print(f'  Over ({total})')
                            break
                    if total <= threshold:
                        # print(f'  Found ({total})')
                        return True
            
            return False

        L = 0
        left = test(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = min(grid_M, grid_N) + 1
        right = test(R)
        if right:
            print(f'Strange, {R=} is true')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = test(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Left')
                (L, left) = (M, mid)
            else:
                print(f'  False: replace Right')
                (R, right) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # L is now the highest possible True value
        return L

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (fencepost error; output exceeded)
# NOTE: Runtime 1200 ms Beats 24.39%
# NOTE: Memory 24.02 MB Beats 9.66%
