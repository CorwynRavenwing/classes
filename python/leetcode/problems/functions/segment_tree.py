        
        # segment tree
        st_size = len(nums)
        st_data = [None] * (4 * st_size)

        def st_combine(a: int, b: int) -> int:
            if a is None:
                return b
            if b is None:
                return a
            return max(a, b)
        
        def st_build(a: List[int], v: int, tL: int, tR: int) -> None:
            # print(f'st_build({v},{tL},{tR})')
            assert v > 0
            if tL == tR:
                st_data[v] = a[tL]
                # print(f'  leaf[{v}]: {st_data[v]}')
            else:
                tM = (tL + tR) // 2
                Left = v * 2
                Right = v * 2 + 1
                st_build(a, Left, tL, tM)
                st_build(a, Right, tM + 1, tR)
                st_data[v] = st_combine(st_data[Left], st_data[Right])
                # print(f'  node[{v}]: {st_data[v]}')

        def st_query(v: int, tL: int, tR: int, L: int, R: int) -> int:
            assert v > 0
            if (L > R):
                return None
            if (L == tL and R == tR):
                return st_data[v]
            tM = (tL + tR) // 2
            Left = v * 2
            Right = v * 2 + 1
            return combine(
                st_query(Left, tL, tM, L, min(R, tM)), 
                st_query(Right, tM + 1, tR, max(L, tM+1), R)
            )
        
        def st_update(v: int, tL: int, tR: int, pos: int, new_val: int) -> None:
            assert v > 0
            if (tL == tR):
                st_data[v] = new_val
            else:
                tM = (tL + tR) // 2
                Left = v * 2
                Right = v * 2 + 1
                if (pos <= tM):
                    st_update(Left, tL, tM, pos, new_val)
                else:
                    st_update(Right, tM + 1, tR, pos, new_val)
                st_data[v] = combine(st_data[Left], st_data[Right])

        def find_leftmost_box_and_update(v: int, tL: int, tR: int, value: int) -> int:
            # print(f'FLBU({v},{tL},{tR},{value})')
            assert v > 0
            # a combination of st_query and st_update
            if st_data[v] < value:
                # print(f'  NO')
                # value is not in this interval
                return None
            if (tL == tR):
                # leaf node
                answer = st_data[v]
                # print(f'  leaf: {answer}')
                st_data[v] = 0
                return answer
            tM = (tL + tR) // 2
            Left = v * 2
            Right = v * 2 + 1
            left_section = find_leftmost_box_and_update(Left, tL, tM, value)
            if left_section is not None:
                st_data[v] = st_combine(st_data[Left], st_data[Right])
                return left_section
            right_section = find_leftmost_box_and_update(Right, tM + 1, tR, value)
            if right_section is not None:
                st_data[v] = st_combine(st_data[Left], st_data[Right])
                return right_section
            return None

        st_build(nums, 1, 0, st_size - 1)
        # print(f'DEBUG: {st_data=}')

        answer = 0
        for F in fruits:
            value = find_leftmost_box_and_update(1, 0, st_size - 1, F)
            # print(f'{F}: {value}')
            if value is None:
                answer += 1
            # print(f'DEBUG: {st_data=}')

        return answer

