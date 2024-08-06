class Solution:
    def robotWithString(self, s: str) -> str:
        
        REV = lambda x: tuple(reversed(tuple(x)))

        minCharFromRight = ''.join(
            REV(accumulate( REV(s), min))
        )
        # print(f'{minCharFromRight=}')
        T = []
        p = ''

        def Op1_S_to_T():
            nonlocal s, T, minCharFromRight
            C = s[0]
            s = s[1:]
            minCharFromRight = minCharFromRight[1:]
            # print(f'OP1: move "{C}" s->T')
            T.append(C)
        
        def Op2_T_to_P():
            nonlocal T, p
            C = T.pop(-1)
            # print(f'OP2: move "{C}" T->p')
            p += C

        while s or T:
            # print(f'{s=} {T=} {p=}\n :"{minCharFromRight}"')
            if s and not T:
                # print('  Empty T')
                Op1_S_to_T()
                continue
            if T and not s:
                # print('  Empty S')
                Op2_T_to_P()
                continue
            # assert both s and t have nonzero length here
            nextS = s[0]
            nextT = T[-1]
            minChar = minCharFromRight[0]
            # print(f'  {nextS=} {minChar=} {nextT=}')
            if nextT <= minChar:
                # print(f'    nextT better than minChar: use it')
                Op2_T_to_P()
                continue
            if minChar < nextS:
                # print(f'    minChar is beter: go towards it')
                Op1_S_to_T()
                continue
            if nextS == minChar <= nextT:
                # print(f'    minChar is here: do both operations')
                Op1_S_to_T()
                Op2_T_to_P()
                continue
            
            print(f'Not sure what comparisons fail to get us here')
            return 'NOPE'
            
        # print(f'{s=} {T=} {p=}\n :"{minCharFromRight}"')

        return p
# NOTE: Runtime 6384 ms Beats 5.35%
# NOTE: Memory 20.13 MB Beats 33.75%

# NOTE: could make this faster by looping through
#   zip(s, minCharFromRight), consuming each character one-by-one,
#   and putting things onto and off of "T" when necessary before
#   repeating the loop.  At the end, eat the rest of T.
