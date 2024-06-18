class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # section 1: find proper row:
        L = 0
        R = len(matrix) - 1
        left = matrix[L][0]
        right = matrix[R][0]
        row = None
        print(f'0 [{L},{R}] = ({left},{right}) {target=}')
        if target == left:
            print(f'found {left=}')
            return True
        if target < left:
            print('  before first row')
            return False
        if target == right:
            print(f'found {right=}')
            return True
        if target > right:
            print('  in (or after) last row')
            row = matrix[R]
        while L + 1 < R and row is None:
            M = (L + R) // 2
            mid = matrix[M][0]
            print(f'R [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
            if mid == target:
                print(f'found {M=} {mid=}')
                return True
            if mid < target:
                print('  replace left')
                (L, left) = (M, mid)
                continue
            if mid > target:
                print('  replace right')
                (R, right) = (M, mid)
                continue
        print(f'Z [{L},{R}] = ({left},{right}) {target=}')
        if target > right:
            print('found row right')
            row = matrix[R]
        elif target > left:
            print('found row left')
            row = matrix[L]
        else:
            raise Exception('didnt find row ?!?')
        
        print(f'{row=} {target=}')
        L = 0
        R = len(row) - 1
        left = row[L]
        right = row[R]
        print(f'1 [{L},{R}] = ({left},{right}) {target=}')
        if target == left:
            print(f'found {left=}')
            return True
        if target == right:
            print(f'found {right=}')
            return True
        while L + 1 < R:
            M = (L + R) // 2
            mid = row[M]
            print(f'B [{L},{M},{R}] = ({left},{mid},{right}) {target=}')
            if mid == target:
                print(f'found {M=} {mid=}')
                return True
            if mid < target:
                print('  replace left')
                (L, left) = (M, mid)
                continue
            if mid > target:
                print('  replace right')
                (R, right) = (M, mid)
                continue
        print(f'X [{L},{R}] = ({left},{right}) {target=}')
        print(f'NOT FOUND')
        return False

