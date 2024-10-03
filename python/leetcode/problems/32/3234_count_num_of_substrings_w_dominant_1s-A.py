class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        intList = tuple(map(int, s))
        oneList = intList
        zeroList = tuple([
            (D + 1) % 2
            for D in intList
        ])
        print(f'{oneList =}')
        print(f'{zeroList=}')

        ACC = lambda x: (0,) + tuple(accumulate(x))
        INDEXES = lambda List, Value: tuple(
            [
                index
                for index, val in enumerate(List)
                if val == Value
            ]
        )

        oneSums = ACC(oneList)
        zeroSums = ACC(zeroList)
        print(f'{oneSums =}')
        print(f'{zeroSums=}')

        oneIndexes = INDEXES(s, '1')
        zeroIndexes = INDEXES(s, '0')
        print(f'{oneIndexes =}')
        print(f'{zeroIndexes=}')

        answer = sum(oneList)   # all length-1 substrings '1' are dominant
        # ... and *no* length-1 substrings '0' are dominant.
        print(f'* {answer=} (== count of input 1s)')

        Len = len(s)

        for L, val in enumerate(intList):
            lenRemain = Len - L
            print(f'{L=} {val=} {lenRemain=}')
            R = L
            # we could easily do an O(N^2) version where we count every number
            # but we'd rather skip forward to only the zeros
            if val == 1:
                zeros = 0
                ones = 1
            else:
                zeros = 1
                ones = 0
            while R < len(intList):
                priorR = R
                zeroPos = bisect_left(zeroIndexes, R + 1)
                # print(f'(DEBUG: bisect_left(zIndex, {R+1}) -> {zeroPos})')
                try:
                    nextZero = zeroIndexes[zeroPos]
                    zeroCheck = intList[nextZero]
                except IndexError:
                    nextZero = len(intList)
                    zeroCheck = 0
                assert zeroCheck == 0
                R = nextZero
                zeroSquared = zeros * zeros
                print(f'  {priorR=} {R=} {zeros=} {ones=} {zeroSquared=} {nextZero=}')
                widthOnesList = R - priorR - 1
                # e.g. [x x x x x 0 1 1 0], zeros are at 5 and 8 (priorR and R)
                #   we want the count of 1's *between* the 0s == 2 == 8 - 5 - 1
                startOnesList = ones + 1
                endOnesList = ones + widthOnesList
                print(f'    {startOnesList=} {widthOnesList=} {endOnesList=}')
                startOnesList = max(zeroSquared, startOnesList)
                if startOnesList <= endOnesList:
                    newSubstrings = endOnesList - startOnesList + 1
                    answer += newSubstrings
                    print(f'    * {newSubstrings=} {answer=}')
                else:
                    print(f'    * no new substrings; {startOnesList=} > {endOnesList=}')
                zeros += 1
                ones = endOnesList
        
        return answer

# NOTE: Acceptance Rate 15.5%
# NOTE: also, fails to work for some cases.  I'm trying a different way
