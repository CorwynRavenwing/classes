class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        def X_spans_Y(X: List[int], Y: List[int]) -> bool:
            (X1, X2) = X
            (Y1, Y2) = Y
            if (X1 < Y1 < X2): return True
            if (X1 < Y2 < X2): return True
            return False
        
        indexesByValue = {}
        for index, value in enumerate(s):
            indexesByValue.setdefault(value, [])
            indexesByValue[value].append(index)
        # print(f'{indexesByValue=}')

        endsByChar = {
            char: (indexes[0], indexes[-1])
            for char, indexes in indexesByValue.items()
        }
        print(f'{endsByChar=}')
        chars = ''.join(sorted(endsByChar.keys()))
        print(f'{chars=}')
        for i in chars:
            for j in chars:
                if j <= i:
                    continue
                print(f'{i}:{j}')
                A = endsByChar[i]
                B = endsByChar[j]
                print(f'  {A} {B}')
                A_spans_B = X_spans_Y(A, B)
                B_spans_A = X_spans_Y(B, A)
                overlap = A_spans_B & B_spans_A
                if overlap:
                    print(f'    overlap')
                elif A_spans_B:
                    print(f'    A contains B')
                elif B_spans_A:
                    print(f'    B contains A')
                else:
                    print(f'    disjoint')
        
        # the idea here would be to take all the pairs
        # that overlap, and merge them with Union Find,
        # and then do take/skip to determine which
        # pairs should be taken.
        
        return ['write', 'me']

# NOTE: Acceptance Rate 44.7% (HARD)

# NOTE: incomplete: not written yet
