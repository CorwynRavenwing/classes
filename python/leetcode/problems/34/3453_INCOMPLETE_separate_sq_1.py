class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        # NOTE: since the answer may be withing 10^-5, we instead search
        # for integers that are 10_000 times larger in the Y direction.
        # X distance is not multipied, which makes the area be 10K times
        # larger rather than 100M times.
        
        def area_below(Y_cutoff: int) -> int:
            # nonlocal squares
            total_area = 0
            for (Xi, Yi, Li) in squares:
                _ = Xi      # throw away Xi
                X_width = Li
                Y_begin = Yi * 10_000
                Y_end = Y_begin + Li * 10_000
                Y_begin = min(Y_begin, Y_cutoff)
                Y_end   = min(Y_end  , Y_cutoff)
                Y_width = Y_end - Y_begin
                # if Y_width == 0:
                #     continue
                area = X_width * Y_width
                print(f'{Xi},{Yi},{Li}: {Y_begin}..{Y_end}={Y_width} -> {area=}')
                total_area += area
            print(f'area_below({Y_cutoff}) = {total_area}')
            return total_area

        max_possible_Y = max([
            Yi * 10_000
            for (Xi, Yi, Li) in squares
        ])

        area_of_everything = area_below(max_possible_Y)

        def isPossible(target: int) -> bool:
            # nonlocal area_of_everything
            area = area_below(target)
            answer = (area * 2) >= area_of_everything
            print(f'iP({target}): below={area}*2 >= {area_of_everything}? {answer}')
            return answer

        L = 0
        left = isPossible(L)
        if left:
            print(f'Strange, {L=} is true')
            return L / 10_000
        R = max_possible_Y
        right = isPossible(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1 / 10_000
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = isPossible(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R / 10_000

# NOTE: Acceptance Rate 40.0% (medium)

# NOTE: INCOMPETE: getting the wrong answer, not sure why
