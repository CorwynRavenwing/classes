class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

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

        answer = []
        while intervals:
            interval1 = intervals.pop(0)
            overlap_group = overlapping(interval1, intervals)
            print(f'{interval1} overlaps with {overlap_group}')
            if not overlap_group:
                answer.append(interval1)
                continue
            non_overlap_group = [
                I
                for I in intervals
                if I not in overlap_group
            ]
            print(f'  ... and not with {non_overlap_group}')
            while overlap_group:
                I = overlap_group.pop(0)
                interval1 = merge(interval1, I)
            intervals = non_overlap_group + [interval1]
        return answer

# NOTE: Runtime 3774 ms Beats 5.51%
# NOTE: Memory 21.22 MB Beats 36.95%
