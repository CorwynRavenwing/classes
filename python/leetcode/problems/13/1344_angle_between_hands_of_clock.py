class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        circle = 360
        halfCircle = circle // 2
        ClockHours = 12
        ClockMinutes = 60
        angleMinutes = circle // ClockMinutes * minutes
        angleHour = circle // ClockHours * hour
        angleHourMin = circle / ClockHours / ClockMinutes * minutes

        angleHourTotal = (angleHour + angleHourMin) % circle
        angle = angleHourTotal - angleMinutes

        print(f'{hour}:{minutes} {angleHour}+{angleHourMin}->{angleHourTotal}')
        print(f'  - {angleMinutes} => {angle}')

        answer = abs(angle) % circle
        if answer > halfCircle:
            # don't measure the outside of the angle
            answer = circle - answer
        
        return answer

# NOTE: Accepted on second Submit (was measuring angle >180deg)
# NOTE: Runtime 0 ms Beats 100.00%
# NOTE: Memory 16.79 MB Beats 7.79%
