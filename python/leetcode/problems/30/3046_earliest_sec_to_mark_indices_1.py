class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        
        # this version is for minimizing something.
        indexList = set(range(1, len(nums)+1))
        # print(f'{indexList=}')
        changesList = set(changeIndices)
        if changesList != indexList:
            print(f'Not all nums are ChangeIndexed: {indexList - changesList}')
            return -1

        REV = lambda x: tuple(reversed(tuple(x)))

        def canMarkEverythingByTargetSecond(target: int) -> bool:
            changesUntilTarget = changeIndices[:target]
            # print(f'\nTEST({target}): {changesUntilTarget=}')
            listUntilTarget = set(changesUntilTarget)
            if listUntilTarget != indexList:
                # print(f'NO: missing changes {indexList} - {listUntilTarget} = {indexList - listUntilTarget}')
                return False
            # print(f'{sorted(indexList)=}')
            changesIndexRev = REV(changesUntilTarget)
            # print(f'{changesIndexRev=}')
            changesPairRev = REV(enumerate(changesUntilTarget))
            # print(f'{changesPairRev=}')
            lastPossible = [
                changesPairRev[
                    changesIndexRev.index(index)
                ]
                for index in indexList
            ]
            # print(f'{lastPossible=}')
            lastPossible = [
                (second + 1, index - 1)     # 1-basis second, 0-basis index
                for second, index in sorted(lastPossible)   # ... ascending seconds
            ]
            # print(f'{lastPossible=}')
            seconds_used = 0
            for second, index in lastPossible:
                N = nums[index]
                # print(f'  {second=} {index=} {N=}')
                seconds_needed = 1 + N
                if second - seconds_used < seconds_needed:
                    # print(f'    No: {second} - {seconds_used} < {seconds_needed=}')
                    return False
                else:
                    seconds_used += seconds_needed

            return True

        L = 0
        left = canMarkEverythingByTargetSecond(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = len(changeIndices)
        right = canMarkEverythingByTargetSecond(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = canMarkEverythingByTargetSecond(M)
            print(f'[{L},{M},{R}] ({left},{mid},{right})')
            if mid:
                print(f'  True: replace Right')
                (R, right) = (M, mid)
            else:
                print(f'  False: replace Left')
                (L, left) = (M, mid)

        print(f'[{L},{R}] ({left},{right})')
        # R is now the lowest possible True value
        return R

# NOTE: Runtime 273 ms Beats 11.32%
# NOTE: Memory 18.42 MB Beats 7.55%
