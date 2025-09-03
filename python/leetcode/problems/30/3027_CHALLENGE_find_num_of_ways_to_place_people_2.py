class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:

        ### Hint 4:

        X = lambda XY: XY[0]
        Y = lambda XY: XY[1]
        SORT_UNIQ = lambda L: tuple(sorted(set(L)))

        x_values = SORT_UNIQ([X(P) for P in points])
        y_values = SORT_UNIQ([Y(P) for P in points])
        # print(f'{x_values=}')
        # print(f'{y_values=}')

        x_translate = {
            value: index
            for index, value in enumerate(x_values)
        }
        y_translate = {
            value: index
            for index, value in enumerate(y_values)
        }
        # print(f'{x_translate=}')
        # print(f'{y_translate=}')
        
        points = [
            (
                x_translate[x],
                y_translate[y],
            )
            for (x, y) in points
        ]

        ### Hint 1:

        BY_X_ASC_Y_DESC = lambda P: (X(P), -Y(P))
        points.sort(key=BY_X_ASC_Y_DESC)
        # print(f'{points=}')

        ### Hint 2 + Hint 3:

        answer = 0
        for i, (Xi, Yi) in enumerate(points):
            # print(f'[{i}] ({Xi},{Yi})')
            m = -1
            for j, (Xj, Yj) in enumerate(points):
                if i >= j:
                    # print(f'  [{i},{j}] invalid')
                    continue
                # print(f'  [{j}] ({Xj},{Yj})')
                if Xi <= Xj:
                    # print(f'\tXi/Xj ok')
                    pass
                else:
                    # print(f'\tXi/Xj invalid')
                    continue
                if Yi >= Yj:
                    # print(f'\t\tYi/Yj ok')
                    if m < Yj:
                        answer += 1
                        m = Yj
                        # print(f'\t\t\tUpdated {m=} {answer=}')
                else:
                    # print(f'\t\tYi/Yj invalid')
                    continue

        return answer

# NOTE: Acceptance Rate 50.7% (HARD)

# NOTE: Accepted on first Run
# NOTE: Accepted on third Submit (Output Exceeded, Time Limit Exceeded)
# NOTE: Runtime 2056 ms Beats 35.29%
# NOTE: Memory 18.51 MB Beats 25.49%
