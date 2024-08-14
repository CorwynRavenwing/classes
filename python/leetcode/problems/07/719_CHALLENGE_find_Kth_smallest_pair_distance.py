class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        # this version is for minimizing something.

        def atLeastKpairsDistancesBelow(target: int) -> bool:
            # print(f'ALKPDB({target}):')
            pairsFound = 0
            for rightIndex, rightVal in enumerate(nums):
                leftVal = rightVal - target
                leftIndex = bisect_left(nums, leftVal)
                if leftIndex >= rightIndex:
                    # print(f'  {leftIndex=} >= {rightIndex=}')
                    continue
                # print(f'  [{leftIndex}:{rightIndex}] ({leftVal},{rightVal})')
                # pair rightIndex with each index from leftIndex to (rightIndex - 1):
                pairsFound += rightIndex - leftIndex
                if pairsFound >= k:
                    # print(f'    {pairsFound=} >= {k=}')
                    return True
            # print(f'    {pairsFound=} < {k=}')
            return False

        L = -1      # b/c 0 might be an actual answer, e.g. [3, 3, 3]
        left = atLeastKpairsDistancesBelow(L)
        if left:
            print(f'Strange, {L=} is true')
            return L
        R = max(nums) - min(nums)   # largest possible distance
        right = atLeastKpairsDistancesBelow(R)
        if not right:
            print(f'Strange, {R=} is false')
            return -1
        print(f'[{L},{R}] ({left},{right})')
        while L + 1 < R:
            M = (L + R) // 2
            mid = atLeastKpairsDistancesBelow(M)
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
# NOTE: Accepted on first Submit :-)
# NOTE: Runtime 121 ms Beats 9.94%
# NOTE: Memory 17.64 MB Beats 16.16%
