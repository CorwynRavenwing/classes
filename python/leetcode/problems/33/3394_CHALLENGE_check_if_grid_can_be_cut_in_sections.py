class Solution:

    # we borrow some code from #3169:

    def merge(self, intervals: List[List[int]], n: int) -> List[List[int]]:

        intervals = list(map(tuple, intervals))
        # print(f'merge({intervals}):')

        # intervals.append((0,0))             # fictional begin-of-range interval
        # intervals.append((n + 1,None))      # fictional end-of-range interval
        # print(f'{intervals=}')
        intervals.sort()
        # print(f'{intervals=}')
        intervals = list(map(tuple, intervals))
        # print(f'{intervals=}')
        for i in range(1, len(intervals)):
            prev_start, prev_end = intervals[i - 1]
            this_start, this_end = intervals[i]
            if prev_start == this_start:
                # intervals share start time: merge, use latest end time
                intervals[i - 1] = None
                intervals[i] = (prev_start, max(prev_end, this_end))
            elif prev_end > this_start:
                # change from #3169: GT not GE
                # signifying that adjacent intervals do NOT overlap

                # intervals overlap: merge, use earliest begin time and latest end time
                intervals[i - 1] = None
                intervals[i] = (prev_start, max(prev_end, this_end))
        print(f'{len(intervals)=}')
        while None in intervals:
            intervals.remove(None)
        print(f'{len(intervals)=}')
        print(f'{intervals=}')

        return intervals

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        x_pairs = []
        y_pairs = []
        for (startX, startY, endX, endY) in rectangles:
            x_pairs.append(
                (startX, endX)
            )
            y_pairs.append(
                (startY, endY)
            )
        x_pairs.sort()
        y_pairs.sort()
        # print(f'{x_pairs=}')
        # print(f'{y_pairs=}')
        x_clean = self.merge(x_pairs, n)
        y_clean = self.merge(y_pairs, n)
        # print(f'{x_clean=}')
        # print(f'{y_clean=}')

        if len(x_clean) >= 3:
            print(f'Success on X')
            return True

        if len(y_clean) >= 3:
            print(f'Success on Y')
            return True

        return False

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (Output Exceeded / Time Exceeded)
# NOTE: Runtime 4794 ms Beats 5.18%
# NOTE: Memory 84.67 MB Beats 5.86%
