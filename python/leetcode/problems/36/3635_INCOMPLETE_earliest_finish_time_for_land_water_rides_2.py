class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
                
        answers = set()
        landEndTimes = [
            start + duration
            for (start, duration) in zip(landStartTime, landDuration)
        ]
        # print(f'{landEndTimes=}')
        for endTime in landEndTimes:
            for (start, duration) in zip(waterStartTime, waterDuration):
                if start < endTime:
                    answers.add(endTime + duration)
                else:
                    answers.add(start + duration)
        waterEndTimes = [
            start + duration
            for (start, duration) in zip(waterStartTime, waterDuration)
        ]
        # print(f'{waterEndTimes=}')
        for endTime in waterEndTimes:
            for (start, duration) in zip(landStartTime, landDuration):
                if start < endTime:
                    answers.add(endTime + duration)
                else:
                    answers.add(start + duration)
        # print(f'{answers=}')

        return min(answers)

# NOTE: Acceptance Rate 39.9% (medium)

# NOTE: tried same code as prior version

# NOTE: Incomplete: works, but TLE for large inputs (testcase 603)

