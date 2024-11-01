class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        def intersectionOf(interval1: Tuple[int,int], interval2: Tuple[int,int]) -> Tuple[int,int]:
            (start1, end1) = interval1
            (start2, end2) = interval2
            start = max(start1, start2)
            end = min(end1, end2)
            if start <= end:
                return (start, end)
            else:
                return ()
        
        answer = []
        while firstList and secondList:
            interval1 = firstList[0]
            interval2 = secondList[0]
            intersect = intersectionOf(interval1, interval2)
            if intersect:
                answer.append(intersect)
            (start1, end1) = interval1
            (start2, end2) = interval2
            if end1 < end2:
                ignore = firstList.pop(0)
            else:
                ignore = secondList.pop(0)

        return answer

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 9 ms Beats 23.07%
# NOTE: Memory 17.47 MB Beats 73.86%
