class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # sort by interval start ASC, then interval end DESC:
        intervals.sort(
            key=lambda x: (x[0], -x[1])
        )

        for i, indexI in enumerate(intervals):
            if indexI is None:
                continue
            
            (C, D) = indexI
            for j, indexJ in enumerate(intervals):
                if i >= j:
                    continue
                if indexJ is None:
                    continue
                
                (A, B) = indexJ

                # From the problem definition:
                # The interval [a, b) is covered by the interval [c, d)
                # if and only if c <= a and b <= d.
                if C <= A and B <= D:
                    print(f'{indexJ} is covered by {indexI}')
                    intervals[j] = None
        
        print(f'\n{intervals=}')
        while None in intervals:
            intervals.remove(None)
        
        return len(intervals)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was a sorting error)
# NOTE: Runtime 23 ms Beats 5.35%
# NOTE: Memory 17.14 MB Beats 49.38%
