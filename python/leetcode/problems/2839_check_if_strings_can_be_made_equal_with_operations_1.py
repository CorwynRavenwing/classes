class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        if s1 == s2:
            return True
        
        (A1, B1, C1, D1) = list(s1)
        (A2, B2, C2, D2) = list(s2)
        print(f'{(A1,B1,C1,D1)=}')
        print(f'{(A2,B2,C2,D2)=}')

        if A1 not in [A2, C2]:
            return False
        if C1 not in [A2, C2]:
            return False
        if B1 not in [B2, D2]:
            return False
        if D1 not in [B2, D2]:
            return False

        return (
            (
                (
                    (A1==A2) and (C1==C2)
                ) or (
                    (A1==C2) and (C1==A2)
                )
            ) and (
                (
                    (B1==B2) and (D1==D2)
                ) or (
                    (B1==D2) and (D1==B2)
                )
            )
        )

