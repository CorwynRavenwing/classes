class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        evens = [N for i, N in enumerate(nums) if i % 2 == 0]
        odds = [N for i, N in enumerate(nums) if i % 2 == 1]
        # print(f'{evens=}')
        # print(f'{odds=}')
        evenLen = len(evens)
        oddLen = len(odds)
        evenCounts = Counter(evens)
        oddCounts = Counter(odds)
        # print(f'{evenCounts=}')
        # print(f'{oddCounts=}')
        evenReplacements = [
            (evenLen - eCount, eNum)
            for eNum, eCount in evenCounts.items()
        ]
        oddReplacements = [
            (oddLen - oCount, oNum)
            for oNum, oCount in oddCounts.items()
        ]
        evenReplacements.sort()
        evenReplacements = evenReplacements[:2]
        oddReplacements.sort()
        oddReplacements = oddReplacements[:2]
        print(f'{evenReplacements=}')
        print(f'{oddReplacements=}')

        answer = max(0, evenLen + oddLen - 1)   # worst case: replace all but 1
        for eReplace, eNum in evenReplacements:
            print(f'even {eNum}: {eReplace}')
            for oReplace, oNum in oddReplacements:
                print(f'  odd {oNum}: {oReplace}')
                if eNum == oNum:
                    print(f'    Equal')
                    possibles = [
                        eReplace + oddLen,   # change these evens and all odds
                        oReplace + evenLen,  # change all evens and these odds
                    ]
                else:
                    print(f'    Different')
                    possibles = [
                        eReplace + oReplace     # change just this set of evens and odds
                    ]
                print(f'      {possibles=}')
                answer = min(
                    answer,
                    min(possibles)
                )
        return answer

