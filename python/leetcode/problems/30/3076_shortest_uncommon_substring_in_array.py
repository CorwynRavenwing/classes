class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:

        REV = lambda x: tuple(reversed(tuple(x)))
        ACC_UNION = lambda x: (set(),) + tuple(accumulate(x, set.union))[:-1]

        def substring_set(s: str) -> Set[str]:
            return {
                s[i:j+1]
                for i in range(len(s))
                for j in range(i, len(s)+1)
            }
        
        SSS = [
            substring_set(A)
            for A in arr
        ]
        leftSet = ACC_UNION(SSS)
        rightSet = REV(ACC_UNION(REV(SSS)))
        otherSet = [
            A | B
            for A, B in zip(leftSet, rightSet)
        ]
        answerSet = [
            Me - Others
            for Me, Others in zip(SSS, otherSet)
        ]
        # print(f'{SSS=}')
        # print(f'{leftSet=}')
        # print(f'{rightSet=}')
        # print(f'{otherSet=}')
        # print(f'arr, SSS, left, right, other:')
        # Z='\n\t'
        # for A, S, L, R, O in zip(arr, SSS, leftSet, rightSet, otherSet):
        #     print(f'{A=}{Z}S={sorted(S)}{Z}L={sorted(L)}{Z}R={sorted(R)}{Z}O={sorted(O)}')
        # print(f'{answerSet=}')
        answers = []
        for AS in answerSet:
            # print(f'{AS=}')
            if not AS:
                answers.append('')
                continue
            length = min(map(len, AS))
            # print(f'  {length=}')
            matches = [
                A
                for A in AS
                if len(A) == length
            ]
            # print(f'  {matches=}')
            answers.append(min(matches))

        return answers

# NOTE: Runtime 754 ms Beats 20.41%
# NOTE: Memory 74.02 MB Beats 9.80%
