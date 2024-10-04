class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return len(points)
        
        def intersectIntervals(I1: Tuple[int,int], I2: Tuple[int,int]) -> Tuple[int,int]:
            (L1, R1) = I1
            (L2, R2) = I2
            L3 = max(L1, L2)
            R3 = min(R1, R2)
            if L3 > R3:
                return None
            else:
                return (L3, R3)
        
        points.sort()
        for i in range(1, len(points)):
            # print(f'{points=}')
            prev = points[i - 1]
            this = points[i]
            both = intersectIntervals(prev, this)
            if both:
                # print(f'Merge {i}')
                points[i - 1] = None
                points[i] = both
        # print(f'{points=}')
        while None in points:
            points.remove(None)
        # print(f'{points=}')

        return len(points)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 2803 ms Beats 5.00%
# NOTE: Memory 53.03 MB Beats 98.97%
