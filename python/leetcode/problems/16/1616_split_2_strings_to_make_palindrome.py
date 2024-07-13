class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def R(S: str) -> str:
            return ''.join(reversed(S))
        
        def splitAtMiddle(S: str) -> Tuple[str,str]:
            L = len(S)
            H = L // 2
            I = L % 2
            return [
                S[:H],
                S[H + I:],
            ]
        
        def similarityCount(s1: str, s2: str) -> int:
            # there are ways of doing this, that short-circuit immediately
            # when reaching the answer.  This version does ALL the comparisons
            same = [
                G == H
                for (G, H) in zip(s1, s2)
            ]
            # print(f'{same=}')
            if False in same:
                index = same.index(False)
                same = same[:index]
            # print(f'{same=}')
            return len(same)
        
        (A1, A2) = splitAtMiddle(a)
        (B1, B2) = splitAtMiddle(b)

        (A1r, A2r) = (R(A1), R(A2))
        (B1r, B2r) = (R(B1), R(B2))

        armLength = len(A1)
        # the others should all be the same
        assert len(B2) == armLength
        assert len(A2r) == armLength
        assert len(B1r) == armLength

        if A1 == A2r:
            print(f'A is a palindrome')
            return True
        if B1 == B2r:
            print(f'B is a palindrome')
            return True
        if A1 == B2r:
            print(f'A first half + B second half')
            return True
        if B1 == A2r:
            print(f'B first half + A second half')
            return True
        
        xAAx = similarityCount(A1r, A2)    # how palindromey is the center of A?
        AxxB = similarityCount(A1, B2r)    # how similar is A to -B?

        xBBx = similarityCount(B1r, B2)    # how palindromey is the center of B?
        BxxA = similarityCount(B1, A2r)    # how similar is B to -A?

        AAAB = AxxB + xAAx    # beginning of A, middle of A, end of B 
        ABBB = AxxB + xBBx    # beginning of A, middle of B, end of B
        BAAA = BxxA + xAAx    # beginning of B, middle of A, end of A 
        BBBA = BxxA + xBBx    # beginning of B, middle of B, end of A
        print(f'{armLength=} {AxxB=} {xAAx=} {AAAB=}')
        print(f'{armLength=} {AxxB=} {xBBx=} {ABBB=}')
        print(f'{armLength=} {BxxA=} {xAAx=} {BAAA=}')
        print(f'{armLength=} {BxxA=} {xBBx=} {BBBA=}')
        for check in [AAAB, ABBB, BAAA, BBBA]:
            if armLength <= check:
                return True

        return False

