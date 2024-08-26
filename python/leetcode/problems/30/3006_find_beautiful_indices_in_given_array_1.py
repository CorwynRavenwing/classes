class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        def findAll(haystack: str, needle: str) -> List[int]:
            # print(f'findAll("{haystack}","{needle}")')
            answers = []
            startPos = 0
            while True:
                try:
                    pos = haystack.index(needle, startPos)
                except ValueError:
                    break
                answers.append(pos)
                startPos = pos + 1
            return answers
        
        allA = findAll(s, a)
        # print(f'{allA=}')
        allB = findAll(s, b)
        # print(f'{allB=}')

        beautiful = []
        bI = 0
        if bI >= len(allB):
            print(f'    {bI=} >= {len(allB)=}.  No answers')
            return []
        for indexA in allA:
            # print(f'{indexA=}')
            while allB[bI] < (indexA - k):
                # print(f'  {bI=} {allB[bI]=} NO')
                bI += 1
                if bI >= len(allB):
                    # print(f'    {bI} >= {len(allB)}.  Stop')
                    break
            if bI >= len(allB):
                # print(f'    {bI} >= {len(allB)}.  Stop')
                break
            if allB[bI] <= (indexA + k):
                # print(f'  {bI=} {allB[bI]=} YES')
                beautiful.append(indexA)

        # beautiful = [
        #     indexA
        #     for indexA in allA
        #     if any([
        #         abs(indexA - indexB) <= k
        #         for indexB in allB[bisect_left(allB,indexA-k):bisect_right(allB,indexA+k)]
        #     ])
        # ]

        return beautiful

# NOTE: Runtime 80 ms Beats 97.61%
# NOTE: Memory 21.20 MB Beats 45.56%
