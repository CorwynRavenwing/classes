class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        def DP_take(index: int, maxes: List[str]) -> int:
            # print(f'  DP_take({index},{maxes})')
            column = strs[index]
            # print(f'    {column =})')
            new_max = tuple([
                (
                    None if V < M else V
                )
                for (V, M) in zip(column, maxes)
            ])
            # print(f'    {new_max=})')
            if None in new_max:
                return None
            else:
                return DP(index + 1, new_max)

        def DP_skip(index: int, maxes: List[str]) -> int:
            # print(f'  DP_skip({index},{maxes})')
            return 1 + DP(index + 1, maxes)

        @cache
        def DP(index: int, maxes: List[str]) -> int:
            # print(f'DP({index},{maxes})')
            try:
                _ = strs[index]
            except IndexError:
                return 0
            answers = [
                DP_take(index, maxes),
                DP_skip(index, maxes),
            ]
            # print(f'DP({index},{maxes}): {answers}')
            while None in answers:
                answers.remove(None)
            answer = min(answers, default=None)
            # print(f'DP({index},{maxes}): {answer}')
            return answer

        # get length before inversion:
        width = len(strs)

        # invert strings;
        strs = tuple(zip(*strs))
        # print(f'inverted: {strs}')

        no_maxes = ('a',) * width
        # print(f'{no_maxes=}')

        answer = DP(0, no_maxes)
        if answer is None:
            raise Exception('error: answer is None')
        return answer



        
        # we borrow some code from #955:

        print(f'MDS({strs})')

        def is_sorted(arr: List[str]) -> bool:
            return arr == sorted(arr)

        def delete_column(strs: List[str], i: int) -> List[str]:
            print(f'dc({strs},{i}):')
            retval = [
                S[:i] + S[i + 1:]   # ... skipping S[i]
                for S in strs
            ]
            print(f'  -> {retval}')
            return retval

        deletes = 0
        i = 0
        while i < len(strs[0]):
            print(f'  loop({i=},{strs})')

            if is_sorted(strs):
                print(f'  already sorted')
                return deletes

            leftHalf = [
                S[:i + 1]
                for S in strs
            ]
            # rightHalf = [
            #     S[i + 1:]
            #     for S in strs
            # ]

            if is_sorted(leftHalf):
                print(f'  leftHalf sorted: keep; next i')
                i += 1
                continue
            else:
                print(f'  leftHalf not sorted: delete {i}')
                # delete this column
                deletes += 1
                strs = delete_column(strs, i)
                continue
        return deletes

# NOTE: Acceptance Rate 59.6% (HARD)

# NOTE: Accepted on third Run (fencepost errors in two directions)
# NOTE: Accepted on third Submit (Output Exceeded; Time Limit Exceeded)
# NOTE: Runtime 967 ms Beats 5.33%
# NOTE: Memory 24.79 MB Beats 14.67%
