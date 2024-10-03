class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        N = len(s)
        SqrtN = int(sqrt(N))
        print(f'{N=} {SqrtN=}')

        answer = 0

        if not s:
            return 0
        
        zeroIndexes = [
            index
            for (index, value) in enumerate(s)
            if value == '0'
        ]
        print(f'{zeroIndexes=}')

        # L, R signify the substring [L .. R], L-inclusive, R-inclusive, [L:R+1]
        # Therefore L is in [0 .. len(s)-1]
        # and R is in [L .. len(s)-1]
        #   L because R can't be before L: the substring can't be empty
        L = 0
        A = s[L]
        R = L
        B = s[R]
        zeroCount = 0
        ZEROSQUARED = lambda: (zeroCount * zeroCount)
        onesCount = 0
        print(f'First window: {B=}')
        if B == '0':
            zeroCount += 1
        elif B == '1':
            onesCount += 1

        while L <= R <= len(s):
            print(f'[{L}..{R}] {answer=} 0={zeroCount} 1={onesCount}')

            if zeroCount > SqrtN:
                print(f'  zeros > {SqrtN}: new window')
                L += 1
                R = L
                print(f'  [{L}..{R}]')
                try:
                    A = s[L]
                except IndexError:
                    print(f'    Ran over end of array')
                    break
                B = s[R]
                zeroCount = 0
                onesCount = 0
                if B == '0':
                    zeroCount += 1
                elif B == '1':
                    onesCount += 1
                print(f'  New window: {B=}')
                print(f'  [{L}..{R}] {answer=} 0={zeroCount} 1={onesCount}')
                if onesCount >= ZEROSQUARED():
                    print(f'    YES: 1({onesCount}) >= 0^2({zeroCount}^2={ZEROSQUARED()})')
                    answer += 1
                else:
                    print(f'    NO: 1({onesCount}) < 0^2(0^{zeroCount}={ZEROSQUARED()})')
                print(f'  [{L}..{R}] {answer=} 0={zeroCount} 1={onesCount}')
                continue

            try:
                nextZeroIndex = s.index('0', R + 1)
            except ValueError:
                # an imaginary extra zero just past the right edge of the array
                nextZeroIndex = len(s)
            onesBeforeNextZero = nextZeroIndex - R - 1  # not counting current R
            print(f'  {nextZeroIndex=} {onesBeforeNextZero=}')
            print(f'  DEBUG: 1BN0 = NZI({nextZeroIndex}) - R({R}) - {1}')

            if onesCount >= ZEROSQUARED():
                print(f'  Dominant ({onesCount} >= {ZEROSQUARED()})')
                # currently dominant: all substrings till NZI are also dominant
                answer += nextZeroIndex - R
                zeroCount += 1  # the "next" zero
                onesCount += onesBeforeNextZero
                R = nextZeroIndex
                continue
            elif onesCount + onesBeforeNextZero >= ZEROSQUARED():
                print(f'  Not Dominant, but will be before NZI')
                # not dominant, but WILL be dominant before NZI
                onesUntilDominant = ZEROSQUARED() - onesCount
                nonDominantToSkip = onesUntilDominant - 1
                if nonDominantToSkip:
                    print(f'  Skip {nonDominantToSkip} of {onesBeforeNextZero}')
                    onesCount += nonDominantToSkip
                    R += nonDominantToSkip
                    print(f'  -> [{L}..{R}] {answer=} 0={zeroCount} 1={onesCount}')
                    onesBeforeNextZero -= nonDominantToSkip
                    print(f'  -> {nextZeroIndex=} {onesBeforeNextZero=}')
                # dominant as of the next char right of R
                answer += nextZeroIndex - R
                zeroCount += 1  # the "next" zero
                onesCount += onesBeforeNextZero
                R = nextZeroIndex
                continue
            else:
                print(f'  Not Dominant')
                # won't be dominant before NZI
                # don't update answer here
                zeroCount += 1  # the "next" zero
                onesCount += nextZeroIndex - R - 1  # not counting current R
                R = nextZeroIndex
                continue

        return answer

# NOTE: Acceptance Rate 15.9%
# NOTE: Giving wrong answers still
