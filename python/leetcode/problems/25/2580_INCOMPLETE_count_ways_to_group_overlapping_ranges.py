class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        
        # we borrow some code from #56:

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
        while ranges:
            interval1 = ranges.pop(0)
            overlap_group = overlapping(interval1, ranges)
            # print(f'{interval1} overlaps with {overlap_group}')
            if not overlap_group:
                answer.append(interval1)
                continue
            non_overlap_group = [
                I
                for I in ranges
                if I not in overlap_group
            ]
            # print(f'  ... and not with {non_overlap_group}')
            while overlap_group:
                I = overlap_group.pop(0)
                interval1 = merge(interval1, I)
            ranges = non_overlap_group + [interval1]
        
        # print(f'after merging, {answer=}')

        mod = 10 ** 9 + 7

        return 2 ** len(answer) % mod
# NOTE: gives a Time Limit Exceeded error for large inputs
