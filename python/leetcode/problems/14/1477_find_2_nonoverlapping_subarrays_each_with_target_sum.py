class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        MAXINT = 2 ** 32 - 1
        lenStartingHere = [MAXINT] * len(arr)
        lenEndingHere = [MAXINT] * len(arr)
        (i, j) = (0, 0)
        A = arr[0]
        B = A
        total = A
        while i <= j < len(arr):
            # print(f'{i=},{j=} {total=}')
            if total == target:
                # print(f'  MATCH {i=} {j=}')
                lenStartingHere[i] = j - i + 1
                lenEndingHere[j] = min(lenEndingHere[j], j - i + 1)
                # fall through here
            if total > target:
                # print(f'  OVER')
                lenStartingHere[i] = MAXINT
                lenEndingHere[j] = min(lenEndingHere[j], MAXINT)
                # fall through here
            if total >= target:
                # picks up both of prior cases
                # print(f'  shrink L')
                total -= A
                i += 1
                if i >= len(arr):
                    # print(f'    End of list')
                    break
                A = arr[i]
                if i > j:
                    # print(f'    bump J')
                    j = i
                    B = A
                    total = A
                continue
            if total < target:
                # print(f'  grow R')
                j += 1
                if j >= len(arr):
                    # print(f'    End of list')
                    break
                B = arr[j]
                total += B
                continue
                
        print(f'{lenStartingHere[:10]=}')
        print(f'  {lenEndingHere[:10]=}')
        
        def getLeftMin(nums: List[int]) -> List[int]:
            # print(f'getLeftMin({nums}):')
            answer = [None] * len(nums)
            for i, N in enumerate(nums):
                if i == 0:
                    answer[i] = N
                    # print(f'{i}: {answer[i]} <- {N}')
                    continue
                answer[i] = min(answer[i - 1], N)
                # print(f'{i}: {answer[i]} <- min({answer[i - 1]}, {N})')
            return answer
        
        def R(X: any) -> any:
            return list(reversed(X))
        
        def getRightMin(nums: List[int]) -> List[int]:
            # print(f'getRightMin({nums}):')
            numsR = R(nums)
            RminR = getLeftMin(numsR)
            Rmin = R(RminR)
            return Rmin

        Lmin = getLeftMin(lenEndingHere)
        Rmin = getRightMin(lenStartingHere)
        print(f'{Lmin[:10]=}')
        print(f'{Rmin[:10]=}')

        shortestLeftExclusive = [MAXINT] + Lmin
        shortestRightInclusive = Rmin

        answers = [
            A + B
            for (A, B) in zip(shortestLeftExclusive, shortestRightInclusive)
            if MAXINT not in (A, B)
        ]
        print(f'{answers=}')
        return min(answers, default=-1)

