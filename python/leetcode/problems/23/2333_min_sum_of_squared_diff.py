class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        K = k1 + k2
        diffs = [
            abs(A - B)
            for (A, B) in zip(nums1, nums2)
        ]
        diffCounts = Counter(diffs)
        diffGroups = list(diffCounts.items())
        diffGroups.sort()
        # print(f'{K}: {diffGroups[-5:]=}')

        while K:
            (largest, Count) = diffGroups.pop(-1)
            if diffGroups:
                (second, Count2) = diffGroups[-1]
                if second == largest:
                    ignore = diffGroups.pop(-1)
                    Count += Count2
                    print(f'  Merge last 2 items: {Count=}')
                    changeSize = 1
                    print(f'A: {changeSize=}')
                elif K >= (Count * (largest - second)):
                    changeSize = (largest - second)
                    print(f'B: {changeSize=}')
                elif K >= Count:
                    # should merge this one and the succeeding
                    changeSize = 1
                    print(f'C: {changeSize=}')
                else:
                    changeSize = 1
                    print(f'D: {changeSize=}')
            elif K >= largest * Count:
                changeSize = largest
                print(f'E: {changeSize=}')
            else:
                changeSize = max(1, K // Count)
                print(f'F: {changeSize=}')
            if largest == 0:
                # put the zero record back in
                bisect.insort(diffGroups, (largest, Count))
                break
            if K >= Count * changeSize:
                print(f'  Delete {changeSize} from group of {Count}')
                largest -= changeSize
                K -= (Count * changeSize)
                bisect.insort(diffGroups, (largest, Count))
            elif K >= Count:
                # Should not be necessary, if changeSize is being set correctly
                print(f'  Delete {1} from group of {Count}')
                largest -= 1
                K -= (Count * 1)
                bisect.insort(diffGroups, (largest, Count))
            else:
                print(f'  Not enough K left for {Count}-size group:')
                print(f'    A: Split off group of {Count - K}')
                bisect.insort(diffGroups, (largest, Count - K))
                largest -= 1
                print(f'    B: Delete 1 from group of {K}')
                bisect.insort(diffGroups, (largest, K))
                K -= K

            # print(f'{K}: {diffGroups[-5:]=}')
        
        Square = lambda x: (x * x)

        newDiffs = [
            Diff
            for (Diff, Count) in diffGroups
            for i in range(Count)
        ]
        print(f'{newDiffs=}')

        squares = list(map(Square, newDiffs))
        print(f'{squares=}')
        
        return sum(squares)
# NOTE: Runtime 928 ms Beats 48.96%
# NOTE: Memory 41.34 MB Beats 11.03%
