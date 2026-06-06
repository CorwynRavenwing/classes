class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        answers = []
        landEndTimes = [
            start + duration
            for (start, duration) in zip(landStartTime, landDuration)
        ]
        print(f'{landEndTimes=}')
        for endTime in landEndTimes:
            for (start, duration) in zip(waterStartTime, waterDuration):
                if start < endTime:
                    answers.append(endTime + duration)
                else:
                    answers.append(start + duration)
        waterEndTimes = [
            start + duration
            for (start, duration) in zip(waterStartTime, waterDuration)
        ]
        print(f'{waterEndTimes=}')
        for endTime in waterEndTimes:
            for (start, duration) in zip(landStartTime, landDuration):
                if start < endTime:
                    answers.append(endTime + duration)
                else:
                    answers.append(start + duration)
        print(f'{answers=}')

        return min(answers)

# NOTE: Acceptance Rate 63.6% (easy)

# NOTE: Accepted on first Run
# NOTE: Accepted on first Submit
# NOTE: Runtime 275 ms Beats 17.92%
# NOTE: Memory 20.57 MB Beats 5.20%
