class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        def ambiguousNumbers(t: str) -> List[str]:
            retval = []
            for i in range(1, len(t) + 1):
                L = t[:i]
                R = t[i:]
                print(f'  an({t}) {L=} {R=}')
                if L[0] == '0' and L != '0':
                    print(f'    L leading 0')
                    continue
                if R == '':
                    retval.append(L)
                    print(f'    -> {L}')
                    continue
                if R[-1] == '0':
                    print(f'    R trailing 0')
                    continue
                decimal = f'{L}.{R}'
                print(f'    -> {decimal}')
                retval.append(decimal)
            return retval
        
        assert s[0] == '('
        assert s[-1] == ')'
        s = s[1:-1]
        print(f'new {s=}')
        retval = []
        for i in range(1, len(s)):
            L = s[:i]
            R = s[i:]
            print(f'AC({s}) {L=} {R=}')
            Lgroup = ambiguousNumbers(L)
            Rgroup = ambiguousNumbers(R)
            print(f'AC({L},{R}) {Lgroup=} {Rgroup=}')
            retval.extend([
                f'({Litem}, {Ritem})'
                for Litem in Lgroup
                for Ritem in Rgroup
            ])

        return retval

