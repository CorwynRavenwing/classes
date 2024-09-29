class MyCalendarThree:

    def __init__(self):
        self.sweepData = Counter()
        return

    def book(self, startTime: int, endTime: int) -> int:
        self.sweepData[startTime] += 1
        self.sweepData[endTime] -= 1
        # print(f'DEBUG: {self.sweepData=}')
        sweepTuples = [
            (time, count)
            for time, count in sorted(self.sweepData.items())
        ]
        # print(f'DEBUG: {sweepTuples=}')
        sweepChanges = [
            count
            for time, count in sweepTuples
        ]
        # print(f'DEBUG: {sweepChanges=}')
        sweepTotals = tuple(accumulate(sweepChanges))
        # print(f'DEBUG: {sweepTotals=}')
        return max(sweepTotals)

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)

# NOTE: Accepted on first Run
# NOTE: Accepted on second Submit (first was Output Exceeded)
# NOTE: Runtime 1386 ms Beats 8.28%
# NOTE: Memory 17.42 MB Beats 43.97%
