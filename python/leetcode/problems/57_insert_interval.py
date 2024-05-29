class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def overlapping(interval1: List[int], intervals: List[List[int]]) -> List[List[int]]:
            (A, B) = interval1
            answers = []
            for I in intervals:
                (X, Y) = I
                if ((
                        (A <= X <= B)
                    ) or (
                        (A <= Y <= B)
                    ) or (
                        (X <= A <= Y)
                    ) or (
                        (X <= B <= Y)
                    )):
                    answers.append(I)
            return answers

        def merge(interval1: List[int], interval2: List[int]) -> List[int]:
            (A, B) = interval1
            (X, Y) = interval2
            return [
                min(A, X),
                max(B, Y)
            ]

        overlap_group = overlapping(newInterval, intervals)
        print(f'{newInterval} overlaps with {overlap_group}')
        non_overlap_group = [
            I
            for I in intervals
            if I not in overlap_group
        ]
        print(f'  ... and not with {non_overlap_group}')
        while overlap_group:
            I = overlap_group.pop(0)
            newInterval = merge(newInterval, I)
        intervals = non_overlap_group
        print(f'calling bisect({intervals}. {newInterval})')
        index = bisect.bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)
        return intervals


