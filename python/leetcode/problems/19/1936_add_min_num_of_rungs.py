class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:

        treadHeights = [
            B - A
            for (A, B) in zip([0] + rungs, rungs)
        ]
        print(f'{treadHeights=}')
        gaps = [
            gap
            for gap in treadHeights
            if gap > dist
        ]
        print(f'{gaps=}')
        newRungs = [
            (gap - 1) // dist
            for gap in gaps
        ]
        print(f'{newRungs=}')
        
        return sum(newRungs)
# NOTE: Runtime 403 ms Beats 48.52%
# NOTE: O(N)
# NOTE: Memory 31.10 MB Beats 10.00%
# NOTE: O(N)
