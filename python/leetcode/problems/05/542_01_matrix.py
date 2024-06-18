class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        size_R = len(mat)
        size_C = len(mat[0])
        print(f'matrix size = {(size_R, size_C)}')

        def isValidPos(pos: List[int]) -> bool:
            (R, C) = pos
            return ((0 <= R < size_R) and (0 <= C < size_C))
        
        def neighborsOf(pos: List[int]) -> List[List[int]]:
            (R, C) = pos
            neighbors = (
                (R-1, C),
                (R+1, C),
                (R, C-1),
                (R, C+1),
            )
            return [
                pos
                for pos in neighbors
                if isValidPos(pos)
            ]

        # print(f'{mat=}')
        dis = [
            [None] * len(row)
            for row in mat
        ]
        # print(f'{dis=}')
        zeros = {
            (R, C)
            for R, row in enumerate(mat)
            for C, val in enumerate(row)
            if val == 0
        }
        print(f'{zeros=}')
        distance = 0
        print(f'{distance=}')
        for (R, C) in zeros:
            # no distance from each zero to itself
            dis[R][C] = 0
        # print(f'{dis=}')
        # check the neighbors of every zero
        to_check = {
            N
            for Z in zeros
            for N in neighborsOf(Z)
        }
        # print(f'{to_check=}')
        while to_check:
            to_check = {
                (R, C)
                for (R, C) in to_check
                if dis[R][C] is None
            }
            distance += 1
            print(f'{distance=}, cells={len(to_check)}')
            new_to_check = set()
            for pos in to_check:
                (R, C) = pos
                print(f'  {pos=} cell={dis[R][C]}')
                if dis[R][C] is not None:
                    # print(f'    already done')
                    continue
                print(f'    -> {distance}')
                dis[R][C] = distance
                new_to_check |= set(neighborsOf(pos))
            to_check = new_to_check
            # print(f'{dis=}')

        return dis

