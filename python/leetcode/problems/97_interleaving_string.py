class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            print(f'incompatible lengths')
            return False
        if s1 == "" and s2 == "" and s3 == "":
            print(f'all blank')
            return True
        if (
            sorted(
                list(s1) + list(s2)
            ) != sorted(
                list(s3)
            )
        ):
            print(f'different letters')
            return False
        
        # zero characters of each string === zero characters of s3
        allowed = {
            0: {(0,0)}
        }
        for k in range(1, len(s1) + len(s2) + 1):
            print(f'{k=}:')
            allowed[k] = set()
            for possible in allowed[k - 1]:
                (P1, P2) = possible
                P3 = P1 + P2
                # NOTE: check for max length here?
                next_s1 = s1[P1] if (P1 < len(s1)) else "-"
                next_s2 = s2[P2] if (P2 < len(s2)) else "-"
                next_s3 = s3[P3] if (P3 < len(s3)) else "-"
                # print(f'  {possible}:{P3} "{next_s1}" "{next_s2}" "{next_s3}"')
                if next_s1 == next_s3:
                    A = (P1 + 1, P2)
                    print(f'    {possible} S1 ({next_s3})-> {A}')
                    allowed[k].add(A)
                if next_s2 == next_s3:
                    A = (P1, P2 + 1)
                    print(f'    {possible} S2 ({next_s3})-> {A}')
                    allowed[k].add(A)
        answers = allowed[len(s1) + len(s2)]
        print(f'{answers=}')
        return len(answers) != 0

