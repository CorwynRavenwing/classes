class Solution:
    def nearestPalindromic(self, n: str) -> str:

        Ni = int(n)

        REV = lambda x: tuple(reversed(tuple(x)))
        REVSTR = lambda x: ''.join(REV(x))

        def buildPalindrome(firstHalf: str, Even: bool) -> str:
            if Even:
                R = REVSTR(firstHalf)
                return firstHalf + R
            else:
                R = REVSTR(firstHalf[:-1])
                return firstHalf + R

        L = len(n)
        Even = (L % 2 == 0)
        halfL = (
            L // 2
            if Even
            else (L + 1) // 2
        )
        firstHalf = n[:halfL]
        print(f'{L=} {Even=} {halfL=} {firstHalf=}')
        answers = []

        P = buildPalindrome(firstHalf, Even)
        Pi = int(P)
        print(f'{P=}')
        if P == n:
            print(f'N was already a palindrome')
            pass
        else:
            answers.append(P)

        nextFirst = str(int(firstHalf) + 1)
        if len(nextFirst) > halfL:
            nextEven = not Even
            if not Even:
                # 999xx -> 1000xx -> 100xxx
                nextFirst = nextFirst[:-1]
        else:
            nextEven = Even
        print(f'  {nextFirst=} {nextEven=}')
        P = buildPalindrome(nextFirst, nextEven)
        print(f'{P=}')
        if P == n:
            print(f'N was already a palindrome')
            pass
        else:
            answers.append(P)

        prevFirst = str(int(firstHalf) - 1)
        if (len(prevFirst) < halfL) or (firstHalf == '1'):
            prevEven = not Even
            if Even:
                prevFirst = str(int(firstHalf+'0') - 1)
                # 100xxx -> 1000xx -> 999xx
        else:
            prevEven = Even
        print(f'  {prevFirst=} {prevEven=}')
        P = buildPalindrome(prevFirst, prevEven)
        print(f'{P=}')
        if P == n:
            print(f'N was already a palindrome')
            pass
        else:
            answers.append(P)

        nDists = [
            (
                abs(int(P) - int(n)),
                int(P),
                P
            )
            for P in answers
        ]
        nDists.sort()
        print(f'{nDists=}')
        (dist, Pi, P) = nDists[0]

        return str(int(P))
# NOTE: Runtime 32 ms Beats 79.76%
# NOTE: Memory 16.59 MB Beats 68.02%
