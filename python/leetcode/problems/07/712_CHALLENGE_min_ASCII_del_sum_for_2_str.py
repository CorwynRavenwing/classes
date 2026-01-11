class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        def min_not_none(L: list) -> int:
            while None in L:
                L.remove(None)
            return min(L, default=None)

        def DP_take_i(i: int, j: int) -> int:
            try:
                A = s1[i]
            except IndexError:
                return None
            ascii = ord(A)
            # print(f'DP({i},{j}): I ({A}={ascii})')
            recurse = DP(i + 1, j)
            if recurse is None:
                return None
            else:
                return ascii + recurse

        def DP_take_j(i: int, j: int) -> int:
            try:
                B = s2[j]
            except IndexError:
                return None
            ascii = ord(B)
            # print(f'DP({i},{j}): J ({B}={ascii})')
            recurse = DP(i, j + 1)
            if recurse is None:
                return None
            else:
                return ascii + recurse

        def DP_skip_both(i: int, j: int) -> int:
            try:
                A = s1[i]
            except IndexError:
                A = None
            try:
                B = s2[j]
            except IndexError:
                B = None
            if A != B:
                # can't skip these two if they're different
                return None
            if A == B == '':
                # end of both strings
                return 0
            else:
                return DP(i + 1, j + 1)

        @cache
        def DP(i: int, j: int) -> int:
            # print(f'DP({i},{j}): A ')
            try:
                A = s1[i]
            except IndexError:
                A = None
            try:
                B = s2[j]
            except IndexError:
                B = None
            if A is None and B is None:
                # ran both out: SUCCESS
                # print(f'DP({i},{j}): B (success)')
                return 0
            # else:
            # use the best of all 3 options:
            answers = [
                DP_take_i(i, j),
                DP_take_j(i, j),
                DP_skip_both(i, j),
            ]
            # print(f'DP({i},{j}): D {answers}')
            retval = min_not_none(answers)
            # print(f'DP({i},{j}): E {retval}')
            return retval

        return DP(0,0)

# NOTE: Acceptance Rate 66.7% (medium)

# NOTE: Third attempt
# NOTE: Accepted on third Run (logic errors)
# NOTE: Accepted on third Submit (Output Exceeded [stopped logs], Time Exceeded [cache])
# NOTE: Runtime 1582 ms Beats 5.14%
# NOTE: Memory 240.02 MB Beats 5.14%
