class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(
            key=lambda x: x[1]  # sort by earliest end time
        )
        answer = 0
        endOfPriorMeeting = float('-inf')   # dawn of time
        for (startI, endI) in intervals:
            print(f'{endOfPriorMeeting}: ({startI},{endI})')
            if startI < endOfPriorMeeting:
                print(f'  delete')
                answer += 1
            else:
                print(f'  keep')
                endOfPriorMeeting = endI
        
        return answer

# NOTE: Runtime 1177 ms Beats 16.77%
# NOTE: Memory 55.53 MB Beats 5.26%
