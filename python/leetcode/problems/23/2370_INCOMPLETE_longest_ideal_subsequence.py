class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        # values = tuple([
        #     alphabet.index(C)
        #     for C in s
        # ])
        # print(f'{values=}')

        # answers = []
        maxLen = 0
        queue = [
            (0, '', s)
        ]
        while queue:
            queue.sort()
            Q = queue.pop(-1)   # highest
            (priorLen, priorString, thisString) = Q
            # print(f'{Q=}')
            if maxLen > priorLen + len(thisString):
                # print(f'  {maxLen=} > {priorLen} + {len(thisString)}')
                continue
            if thisString == '':
                # print(f'  Found {priorLen}: "{priorString}"')
                # answers.append(priorLen)
                maxLen = max(maxLen, priorLen)
                continue
            if priorString == '':
                # print(f'  No prior: do both')
                firstChar = thisString[0]
                # print(f'      Move one character over')
                queue.append(
                    (
                        priorLen + 1,
                        priorString + firstChar,
                        thisString[1:],
                    )
                )
                # print(f'      Delete one character')
                queue.append(
                    (
                        priorLen,
                        priorString,
                        thisString[1:],
                    )
                )
            else:
                # print(f'  prior exists: check last character')
                lastChar = priorString[-1]
                firstChar = thisString[0]
                lastNum = alphabet.index(lastChar)
                firstNum = alphabet.index(firstChar)
                diff = abs(firstNum - lastNum)
                ok = (diff <= k)
                # print(f'    {lastChar}({lastNum}), {firstChar}({firstNum}): {diff}({ok})')
                if ok:
                    # print(f'      Move one character over')
                    queue.append(
                        (
                            priorLen + 1,
                            priorString + firstChar,
                            thisString[1:],
                        )
                    )
                # print(f'      Delete one character')
                queue.append(
                    (
                        priorLen,
                        priorString,
                        thisString[1:],
                    )
                )
        # print(f'{answers=}')
        return maxLen
# NOTE: this is incomplete because I'm getting Time Limit Exceeded.
# NOTE: we should do a DP for 'longest legal subsequence ending here'
