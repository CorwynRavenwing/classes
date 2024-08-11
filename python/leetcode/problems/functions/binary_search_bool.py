
    # this version is for minimizing something.

        def test(target: int) -> bool:
            # put the test here.
            # Here, True is good and happens for higher numbers
            return True
        
        L = min(nums)
        left = test(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(nums)
        right = test(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = test(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

    # this version is for maximizing something.

        def test(target: int) -> bool:
            # put the test here.
            # Here, True is good and happens for lower numbers
            return True

        nums.sort()

        L = 0
        left = test(L)
        if not left:
            print(f'Strange, {L=} is false')
            return L
        R = len(nums) + 1
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

